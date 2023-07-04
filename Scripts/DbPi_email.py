import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from smtplib import SMTPException

def send_an_email():
    toaddr = 'jeffrey.samuel@protonmail.com'      # To id 
    me = 'doorbelbot1111@gmail.com'          # your id
    subject = "Someone is at your doorbell"              # Subject

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "Someone is at your doorbell "
    #msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("i0.jpg", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="i0.jpg"')   # File name and format name
    msg.attach(part)

    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(user = 'doorbelbot1111@gmail.com', password = 'tcjmjegzzknshcrg')  # User id & password
       s.sendmail(me, toaddr, msg.as_string())
       s.quit()
    except smtplib.SMTPException as error:
          print ("Error")                # Exception

send_an_email()



