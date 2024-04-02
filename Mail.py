import smtplib,ssl
from email.message import EmailMessage
from Get_Last import get_dernier
import pandas as pd

df= pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\final_data.csv")
df = get_dernier(df)
#Premier essai bugué
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('vintedbot079@gmail.com', 'rima atpl jxum yedp')
"""server.sendmail(from_addr='vintedbot079@gmail.com',
                to_addrs='carlfogue193@gmail.com',
                subject= ": vinted bot \nCe message est un bot\nJespere que tu as bienre cu les produits")
"""

email_password = 'rima atpl jxum yedp'
email_sender = 'vintedbot079@gmail.com'
email_receiver = 'carlfogue193@gmail.com'

prix = df["Prix"].iloc[0]
marque = df["Marque"].iloc[0]
taille = df["Taille"].iloc[0]
ajout = df["Date d'ajout"].iloc[0]

subject = "test envoie mail bot"
body = """Ouvre vite ce mail
Urgent 
\nPrix : {prix}
\nMarque : {marque}
\nTaille : {taille}
\nAjout : {ajout}
!!!!

"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



