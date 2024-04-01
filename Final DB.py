import requests
from bs4 import BeautifulSoup
import time, random
user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
import pandas as pd
import selenium
from urllib.error import URLError, HTTPError


def get_page(urlpage):
    # Avoid getting ban
    time.sleep(2 + random.uniform(0, 3))
    #The post might be deleted when we want to access it, doing this allow the bot to keep working even if the link brings to nowhere
    try:
         # Get the html from the webpage
        res = requests.get(urlpage, headers=user_agent)
        # Parse the html
        soup = BeautifulSoup(res.text, 'html.parser')
        
        #Try to get the price, except a bunch of error (we're never too cautious)
        try:
            prix = soup.find('h1', class_='web_ui__Text__text web_ui__Text__heading web_ui__Text__left').text.strip()
        except (AttributeError, TypeError, TimeoutError, ValueError):
            prix = "NaN"

        try:
            marque = soup.find('span', itemprop='name').text
        except (AttributeError, TypeError, TimeoutError, ValueError):
            marque = "NaN"

        try:
            taille = soup.find('div', class_='details-list__item-value', itemprop='size').text.strip()
        except (AttributeError, TypeError, TimeoutError, ValueError):
            taille = "NaN"

        try:
            etat = soup.find('div', class_='details-list__item-value', itemprop='condition').text.strip()
        except (AttributeError, TypeError, TimeoutError, ValueError):
            etat = "NaN"

        try:
            couleur = soup.find('div', class_='details-list__item-value', itemprop='color').text.strip()
        except (AttributeError, TypeError, TimeoutError, ValueError):
            couleur = "NaN"

        try:
            localisation = soup.find('div', class_='details-list__item',
                                     attrs={"data-testid": "item-details-location"}).text.strip()
        except (AttributeError, TypeError, TimeoutError, ValueError):
            localisation = "NaN"

        try:
            vues = soup.find('div', class_='details-list__item',
                             attrs={"data-testid": "item-details-view_count"}).text.strip()
        except (AttributeError, TypeError, TimeoutError, ValueError):
            vues = "NaN"

        try:
            date_ajout = soup.find('div', class_='details-list__item',
                                   attrs={"data-testid": "item-details-uploaded_date"}).text.strip()
        except (AttributeError, TypeError, TimeoutError, ValueError):
            date_ajout = "NaN"

        return {
            "Prix": prix,
            "Marque": marque,
            "Taille": taille,
            "État": etat,
            "Couleur": couleur,
            "Localisation": localisation,
            "Vues": vues,
            "Date d'ajout": date_ajout
        }
    except (ConnectionError, TimeoutError, PermissionError, URLError, HTTPError):
        return {
            "Prix": "NaN",
            "Marque": "NaN",
            "Taille": "NaN",
            "État": "NaN",
            "Couleur": "NaN",
            "Localisation": "NaN",
            "Vues": "NaN",
            "Date d'ajout": "NaN"
        }
#This fonction just takes all the IRL we scrapped before and return a Pandas Dataframe containing bunch of information
def scrape_data(df):
    data_list = []
    for urlpage in df["Lien"]:
        data = get_page(urlpage)
        data_list.append(data)
    return(pd.DataFrame(data_list))

df = pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\vinted_data.csv")
df_3 = df.head(3)

#Call The function
final_df = scrape_data(df)

print(final_df)

# Enregistrer la DataFrame dans un fichier CSV dans le même dossier que le fichier original
final_df.to_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\final_data.csv", index=False)
