import pandas as pd
from bs4 import BeautifulSoup
import time
import random
import requests
from bs4 import BeautifulSoup


# Fonction pour extraire les informations d'une page Vinted à partir du lien
def scrapper_vinted(lien):
    response = requests.get(lien)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Exemple : Extraire le nom de l'article
        nom_article = soup.find('h1', class_='title-1111').text.strip()

        # Exemple : Extraire le prix de l'article
        prix_article = soup.find('span', class_='text-bold').text.strip()

        # Exemple : Afficher le nom et le prix de l'article
        print("Nom de l'article:", nom_article)
        print("Prix de l'article:", prix_article)
    else:
        print("Erreur lors de la requête à", lien)


# Fonction pour itérer sur toutes les lignes de la base de données et appeler le scraper
def scraper_base_de_donnees(dataframe):
    for lien in dataframe['Lien']:
        scrapper_vinted(lien)


# Charger votre base de données avec pandas
# Remplacez 'votre_fichier.csv' par le chemin de votre fichier CSV contenant la colonne "Lien"
dataframe = pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\vinted_data.csv")

# Appel de la fonction pour scraper la base de données
scraper_base_de_donnees(dataframe)