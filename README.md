# ftnt_WordoftheDay
Create a word of the day password for wifi and email it out

Must create an API user that can edi user and devices.

In the Fortigate create a guest user and enter it in worduser = "<guest-user>"

When setting up the Wifi on the Fortigate, you can share the username or modify the html of the login page to automatically set the username and hide that field by using the HTML hidden type.  Then the user will just need to enter the password.

Setup cron to run on a regular basis and SMTP to send the password to the required users.
