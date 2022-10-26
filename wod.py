from random_word import RandomWords
import requests
import smtplib, ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#==============
#Enter Variables for FGT Access
ip="<fortigate ip>"
apikey = "<api user key>"
worduser = "<guest username>"
#==============

#Create API URL and Header - change port if using different admin port than 443
url = "https://%s:443/api/v2/cmdb/user/local/%s" % (ip,worduser)
headers = {'Authorization': 'Bearer 0m904fwNfppGwcQtxpdQfyNcg9q087',
  'Content-Type': 'text/plain'}

#Generate Random Word
r = RandomWords()
word = r.get_random_word(hasDictionaryDef="true", minLength=8, maxLength=10, minCorpusCount=1, maxCorpusCount=10)

#debug output to show word
#print (word)

#Generate API Payload with new Password
payload = str("{\"passwd\" : \"%s\"}" % (word))

#Make API Call
response = requests.request("PUT", url, headers=headers, data=payload, verify=False)


#Capture the Word and ouptut to file for backup
f = open("wod.txt", "w")
f.write(word)
f.write(response.text)
f.close()

#Send Email with Password - gmail settings
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "<from address>@gmail.com"
receiver_email = "<to address>k@gmail.com"
password = "<sender password>"
message = """\
Subject: Word of the Day

The word of the day today is: %s""" % (word)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
