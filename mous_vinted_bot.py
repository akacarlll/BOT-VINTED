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
MAX_PRIX = 6
URL = f"https://www.vinted.fr/vetements?search_text={RECHERCHE}"
SELECTEUR_LIEN = "a.new-item-box__overlay"
SELECTEUR_PRIX = "div.new-item-box__title > .title-content > p"
SELECTEUR_ARTICLES = "div.feed-grid__item"
TEMPS_ACTUALISATION = 600
TO_EMAIL='lafdhalahmed@gmail.com'
SENDER_MAIL='moustapha.aillal@etu.unistra.fr'
OBJET_MAIL='Nouvelle annonce vinted'


def send_notification_by_mail(link,price):
    message = Mail(
    from_email=SENDER_MAIL,
    to_emails=TO_EMAIL,
    subject=OBJET_MAIL,
    html_content=f'<strong>Une nouvelle annonce est disponible prix {price} voici le lien{link}</strong>'
    )
    try:
        sg = SendGridAPIClient('walou')
        response = sg.send(message)
        print("mail envoyé")
    except Exception as e:
        print(e)


def extract_float_value(price_string):
    price_without_currency=price_string.split()[0]
    price_to_universe_format=price_without_currency.replace(',', '.')
    print(price_to_universe_format)
    return float(price_to_universe_format)

def scrape_vinted_for_new_listings(url, last_seen_title=None):
    options = Options()
    options.headless = True  # Exécute en mode sans tête pour économiser des ressources
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)  # Attendre que la page charge

    # Trouver les annonces et extraire le titre de la première annonce
    listings = driver.find_elements(By.CSS_SELECTOR, SELECTEUR_ARTICLES)
    if listings:
        for listing in listings:
            prix_temp = extract_float_value(listing.find_element(By.CSS_SELECTOR, SELECTEUR_PRIX).text)
            if prix_temp < MAX_PRIX:
                link=listing.find_element(By.CSS_SELECTOR, SELECTEUR_LIEN).get_attribute("href")
                driver.quit()
                return link,prix_temp
    driver.quit()
    return None,None

def main():

    last_seen_title = None

    while True:
        first_listing_link,prix = scrape_vinted_for_new_listings(URL, last_seen_title)
        if first_listing_link != last_seen_title and first_listing_link is not None:

            send_notification_by_mail(first_listing_link,prix)

        time.sleep(TEMPS_ACTUALISATION)

if __name__ == "__main__":
    print("main")
    main()