import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from plyer import notification
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail





RECHERCHE="chaussure nike air jordan"
MAX_PRIX = 50
URL = f"https://www.vinted.fr/vetements?search_text={RECHERCHE}"
SELECTEUR_LIEN = "a.new-item-box__overlay"
SELECTEUR_PRIX = "div.new-item-box__title > .title-content > p"
SELECTEUR_ARTICLES = "div.feed-grid__item"
TEMPS_ACTUALISATION = 600
TO_EMAIL='moustaphaallal80@gmail.com'
SENDER_MAIL='moustapha.aillal@etu.unistra.fr'
OBJET_MAIL='Nouvelle annonce trouvée'
MAX_SIZE_ELEMENT='42'

def send_notification_by_mail(link,price,localisation_vendeur,nb_articles_vendeur,link_seller):
    message = Mail(
    from_email=SENDER_MAIL,
    to_emails=TO_EMAIL,
    subject=OBJET_MAIL,
    html_content= f"""\
     <br>
    🎉 Nouvelle annonce trouvée ! 🎉  <br>

    Prix : {price} €  <br>
    Lien de l'annonce : {link} <br>

    📍 Localisation du vendeur : {localisation_vendeur}  <br>
    📦 Nombre d'articles publiés par le vendeur : {nb_articles_vendeur} articles  <br>
    📞 Contacter le vendeur : {link_seller}  <br>
    N'attendez pas pour jeter un œil ! Cette offre pourrait etre intéressante. <br>
    """)
    try:
        sg = SendGridAPIClient('walou')
        response = sg.send(message)
        print("mail envoyé")
    except Exception as e:
        print(e)


def extract_float_value(price_string):
    price_without_currency=price_string.split()[0]
    price_to_universe_format=price_without_currency.replace(',', '.')
    return float(price_to_universe_format)

def scrape_vinted_for_new_listings(url, last_seen_title=None):
    options = Options()
    options.headless = True  # Exécute en mode sans tête pour économiser des ressources
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Attendre que la page charge

    listings = driver.find_elements(By.CSS_SELECTOR, SELECTEUR_ARTICLES)
    if listings:
        for listing in listings:
            prix_temp = extract_float_value(listing.find_element(By.CSS_SELECTOR, SELECTEUR_PRIX).text)
            size_element = listing.find_element(By.CSS_SELECTOR, "[data-testid$='--description-title']").text
            if prix_temp < MAX_PRIX and size_element==MAX_SIZE_ELEMENT:
                link=listing.find_element(By.CSS_SELECTOR, SELECTEUR_LIEN).get_attribute("href")
                seller_link = listing.find_element(By.CSS_SELECTOR, "a.web_ui__Cell__cell.web_ui__Cell__narrow.web_ui__Cell__link").get_attribute("href")
                driver.quit()
                return link,prix_temp,seller_link
    driver.quit()
    return None,None,None


def get_nombre_arrticle(nombre_article):
    if nombre_article is None:
        return None
    return nombre_article.split()[0]

def get_seller_informations(link):
    options = Options()
    options.headless = True  # Exécute en mode sans tête pour économiser des ressources
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(5)  # Attendre que la page charge
    location_element = driver.find_element(By.XPATH, "//div[@data-testid='profile-location-info--content']").text
    nombre_article = driver.find_element(By.CSS_SELECTOR, "h2.web_ui__Text__text.web_ui__Text__title.web_ui__Text__left").text
    return location_element,get_nombre_arrticle(nombre_article)

def main():

    last_seen_title = None

    while True:
        first_listing_link,prix ,seller_link= scrape_vinted_for_new_listings(URL, last_seen_title)
        if first_listing_link != last_seen_title and first_listing_link is not None:
            seller_city,nombre_items=get_seller_informations(seller_link)
            send_notification_by_mail(first_listing_link,prix,seller_city,nombre_items,seller_link)
            pass
        time.sleep(TEMPS_ACTUALISATION)

if __name__ == "__main__":
    print("main")
    main()