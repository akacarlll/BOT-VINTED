import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

RESEARCH = "chaussure nike air jordan"
MAX_PRICE = 50
URL = f"https://www.vinted.fr/vetements?search_text={RESEARCH}"
LINK_SELECTOR = "a.new-item-box__overlay"
SELLER_LINK_SELECTOR = "a.web_ui__Cell__cell.web_ui__Cell__narrow.web_ui__Cell__link"
PRICE_SELECTOR = "div.new-item-box__title > .title-content > p"
ITEMS_SELECTOR = "div.feed-grid__item"
SIZE_SELECTOR = "[data-testid$='--description-title']"
NUMBER_ITEMS_SOLD_SELECTOR = (
    "h2.web_ui__Text__text.web_ui__Text__title.web_ui__Text__left"
)
LOCATION_SELECTOR = "//div[@data-testid='profile-location-info--content']"
REFRESH_TIME = 600
RECEIVER_EMAIL = ""
SENDER_MAIL = ""
MAIL_SUBJECT = "Nouvelle annonce trouvée"
RESEARCH_SIZE = "42"
KEY = ""


def send_notification_by_mail(
    link, price, seller_location, number_of_items_sold, seller_link
):
    message = Mail(
        from_email=SENDER_MAIL,
        to_emails=RECEIVER_EMAIL,
        subject=MAIL_SUBJECT,
        html_content=f"""\
     <br>
    🎉 Nouvelle annonce trouvée ! 🎉  <br>

    price : {price} €  <br>
    Lien de l'annonce : {link} <br>

    📍 Localisation du vendeur : {seller_location}  <br>
    📦 Nombre d'articles publiés par le vendeur : {number_of_items_sold} articles  <br>
    📞 Contacter le vendeur : {seller_link}  <br>
    N'attendez pas pour jeter un œil ! Cette offre pourrait etre intéressante. <br>
    """,
    )
    try:
        sg = SendGridAPIClient(KEY)
        response = sg.send(message)
    except Exception as e:
        print(e)


def extract_float_value(price_string):
    price_without_currency = price_string.split()[0]
    price_to_universal_format = price_without_currency.replace(",", ".")
    return float(price_to_universal_format)


def scrape_vinted_for_new_listings(url, last_seen_title=None):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    listings = driver.find_elements(By.CSS_SELECTOR, ITEMS_SELECTOR)
    if listings:
        for listing in listings:
            temp_price = extract_float_value(
                listing.find_element(By.CSS_SELECTOR, PRICE_SELECTOR).text
            )
            element_size = listing.find_element(By.CSS_SELECTOR, SIZE_SELECTOR).text
            if temp_price < MAX_PRICE and element_size == RESEARCH_SIZE:
                link = listing.find_element(
                    By.CSS_SELECTOR, LINK_SELECTOR
                ).get_attribute("href")
                seller_link = listing.find_element(
                    By.CSS_SELECTOR, SELLER_LINK_SELECTOR
                ).get_attribute("href")
                driver.quit()
                return link, temp_price, seller_link

    driver.quit()
    return None, None, None


def get_number_items_sold(number_items_description):
    if number_items_description is None:
        return None
    return number_items_description.split()[0]


def get_seller_informations(link):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(5)
    location_element = driver.find_element(By.XPATH, LOCATION_SELECTOR).text
    number_items_description = driver.find_element(
        By.CSS_SELECTOR, NUMBER_ITEMS_SOLD_SELECTOR
    ).text
    return location_element, get_number_items_sold(number_items_description)


def main():

    last_seen_title = None

    while True:
        first_listing_link, price, seller_link = scrape_vinted_for_new_listings(
            URL, last_seen_title
        )
        if first_listing_link != last_seen_title and first_listing_link is not None:
            seller_location, number_items_sold = get_seller_informations(seller_link)
            send_notification_by_mail(
                first_listing_link,
                price,
                seller_location,
                number_items_sold,
                seller_link,
            )
            last_seen_title=first_listing_link
        time.sleep(REFRESH_TIME)


if __name__ == "__main__":
    print("The Scraper is launched")
    main()