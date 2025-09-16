import smtplib
from email.message import EmailMessage
import ssl
import getpass
import os
from dotenv import load_dotenv

#load env variables
load_dotenv()

sender = "protien292@gmail.com"
password = os.getenv("PASSWORD")
print(password)

# creates an email object that we want to send
message = EmailMessage()
message["From"] = sender
message["To"] = "mkonu@sas.upenn.edu"
message["Subject"] = "Test"
message.set_content("Hello World")

# creation of our email server(IP address and port on the server)
server_address = "smtp.gmail.com"
port = 465
# creating a connection with the aformentioned server via a secure "line"
context = ssl.create_default_context()
try:
    server = smtplib.SMTP_SSL(server_address, port, context=context)
    # logging into our email server
    server.login(sender, password)
    # sending our email
    server.send_message(message)
except Exception as e:
    print(e)
