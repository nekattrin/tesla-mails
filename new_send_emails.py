import ssl, smtplib
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()
    password = os.getenv('PASSWORD')
    username = 'n@gmail.com'
    receiver = 'n@gmail.com'

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)