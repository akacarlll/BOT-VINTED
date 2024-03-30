import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from plyer import notification

RECHERCHE="chaussure nike air jordan"
MAX_PRIX = 30
URL = f"https://www.vinted.fr/vetements?search_text={RECHERCHE}"
SELECTEUR_LIEN = "a.new-item-box__overlay"
SELECTEUR_PRIX = "div.new-item-box__title > .title-content > p"
SELECTEUR_ARTICLES = "div.feed-grid__item"
TEMPS_ACTUALISATION = 600


def scrape_vinted_for_new_listings(url, last_seen_title=None):
    options = Options()
    options.headless = True  # Exécute en mode sans tête pour économiser des ressources
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    time.sleep(5)  # Attendre que la page charge
    
    # Trouver les annonces et extraire le titre de la première annonce
    listings = driver.find_elements(By.CSS_SELECTOR, SELECTEUR_ARTICLES)
    if listings:
        first_listing_link =listings[0].find_element(By.CSS_SELECTOR, SELECTEUR_LIEN).get_attribute("href")
        prix = listings[0].find_element(By.CSS_SELECTOR, SELECTEUR_PRIX).text
    else:
        price= None
        first_listing_link = None
    
    driver.quit()
    
    return first_listing_link,prix

def main():
    
    last_seen_title = None
    
    while True:
        first_listing_link,prix = scrape_vinted_for_new_listings(URL, last_seen_title)
        print("first_listing_link",first_listing_link)
        print("prix",prix)
        break
        
        if first_listing_link != last_seen_title and first_listing_link is not None:
            notification.notify(
                title='Nouvelle annonce sur Vinted !',
                message=f'Une nouvelle annonce a été trouvée : {first_listing_link}',
                app_name='Vinted Scraper'
            )
            last_seen_title = first_listing_link
        
        time.sleep(TEMPS_ACTUALISATION) 

if __name__ == "__main__":
    main()
