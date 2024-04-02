import smtplib,ssl
from email.message import EmailMessage
from Get_Last import get_dernier
import pandas as pd


def send_email(prix, marque, taille, ajout, sender_email, sender_password, receiver_email):
    subject = "Le BOT a trouvé un nouvel article"
    body = f"""Ouvre vite ce mail
    Urgent 
    \nPrix : {prix}
    \nMarque : {marque}
    \nTaille : {taille}
    \nAjout : {ajout}
    !!!!
    """

    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)
def main2():
    df = pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\final_data.csv")
    df = get_dernier(df)

    email_password = 'rima atpl jxum yedp'
    email_sender = 'vintedbot079@gmail.com'
    email_receiver = 'carlfogue193@gmail.com'

    prix = df["Prix"].iloc[0]
    marque = df["Marque"].iloc[0]
    taille = df["Taille"].iloc[0]
    ajout = df["Date d'ajout"].iloc[0]

    send_email(prix, marque, taille, ajout, email_sender, email_password, email_receiver)

# Appeler la fonction main si ce script est exécuté en tant que programme principal
if __name__ == "__main__":
    main2()


