import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# server = smtplib.SMTP('poczta.int.pl')
# server.login('isapy@int.pl', 'isapython;')
# server.send_message(mail)
# server.quit()
# img_data = open(r'D:\obrazy\graficzki\papajo.jpg', 'rb').read()
# mail = MIMEMultipart()
# mail['Subject'] = 'Elko'
# mail['To'] = '************'
# mail['From'] = 'matikacprowicz@gmail.com'
# tekst = MIMEText('Eluwina')
# mail.attach(tekst)
# image = MIMEImage(img_data, name=os.path.basename(r'D:\obrazy\graficzki\papajo.jpg'))
# mail.attach(image)
# i = 0
# while i < 5:
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as serwer:
#         serwer.login('matikacprowicz@gmail.com', '**********')
#         serwer.send_message(mail)
#     i+=1

def email_send(email, files):
    mail = MIMEMultipart()
    mail['Subject'] = 'Email wygenerowany automatycznie - pobeiraczek'
    mail['To'] = email
    mail['From'] = 'isapy@int.pl'
    tekst = MIMEText('Wyniki wyszukiwania na pobieraczku.')
    mail.attach(tekst)
    mail.attach(files)
    with smtplib.SMTP('poczta.int.pl') as server:
        server.login('isapy@int.pl', 'isapython')
        server.send_message(mail)
