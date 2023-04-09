import ssl
import smtplib
from email.message import EmailMessage
import mysecrets

def send_response(chatResp, name):

    sender = "aman.squ@gmail.com"
    recv = "s128037@student.squ.edu.om"
    subject = "Survey Response"
    password = mysecrets.gapp_sec
    body = f'''
    Hello {name}, 
    
    {chatResp}
    '''

    em = EmailMessage() 
    em['From'] = sender
    em ['To'] = recv
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recv, em.as_string())




