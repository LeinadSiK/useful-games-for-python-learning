# lgip zssb qejn jstq

from email.message import EmailMessage
from email.mime.image import MIMEImage
import ssl
import smtplib

sender = 'leinad.sik@gmail.com'
receiver = 'leinad.sik@gmail.com'
app_password = 'lgip zssb qejn jstq'

subject = input('Subject: ')
body = input('Body: ')

message = EmailMessage()
message['Subject'] = subject
message['From'] = sender
message['To'] = receiver
message.set_content(body)

attach_image = input('Attach image? (y/n): ')
if attach_image.startswith('y'):

    with open(r'C:\Users\dkiss\Desktop\me.jpg', 'rb') as img:
        img_data = img.read()
    message.add_attachment(img_data, maintype='image', subtype='jpeg', filename='image.jpg')

print('Sending email...')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, app_password)
    server.send_message(message)
    print('Email sent!')



