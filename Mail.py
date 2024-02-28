import smtplib,ssl
from email.message import EmailMessage
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('vintedbot079@gmail.com', 'rima atpl jxum yedp')

email_password = 'rima atpl jxum yedp'
email_sender = 'vintedbot079@gmail.com'
email_receiver = 'carlfogue193@gmail.com'

subject = "test envoie mail bot"
body = """Ouvre vite ce mail
Urgent 
!!!!

"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

"""server.sendmail(from_addr='vintedbot079@gmail.com',
                to_addrs='carlfogue193@gmail.com',
 
                subject= ": vinted bot \nCe message est un bot\nJespere que tu as bienre cu les produits")
"""

