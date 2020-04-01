import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# server = smtplib.SMTP('poczta.int.pl')
# server.login('isapy@int.pl', 'isapython;')
# server.send_message(mail)
# server.quit()
mail = MIMEMultipart()
mail['Subject'] = 'Temat'
mail['To'] = 'isapy@int.pl'
mail['From'] = 'isapy@int.pl'
txt = MIMEText('Siemka')
mail.attach(txt)
with smtplib.SMTP('poczta.int.pl') as serwer:
    serwer.login('isapy@int.pl', 'isapython;')
    serwer.send_message(mail)