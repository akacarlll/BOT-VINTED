
import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd




options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

#Lance en arrière plan si True
options.headless = True

#Modifie la taille de la fenêtre
options.add_argument("window-size=1200x600")

#Chemin à suivre pour trouver le programme Chrome_Driver

PATH = "C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\chromedriver_win32\\chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service, options = options)



#Classe qui permet de colorer les sorties du code
class Spy():
    gris = "\033[1;30;1m"
    rouge = "\033[1;31;1m"
    vert = "\033[1;32;1m"
    jaune = "\033[1;33;1m"
    bleu = "\033[1;34;1m"
    violet = "\033[1;35;1m"
    cyan = "\033[1;36;1m"
    blanc = "\033[1;0;1m"


user_agent = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

global dict_order, dict_catalog, dict_size, dict_color, dict_brand, dict_condition
dict_order = dict({'relevance': '&order=relevance','decreasing price' : '&order=price_high_to_low',\
'increasing price' : '&order=price_low_to_high', 'most recent first' : '&order=newest_first'})
dict_catalog = dict({'men':'&catalog[]=5', 'women':'&catalog[]=1904', 'children': '&catalog[]=1193', \
'home':'&catalog[]=1918'})
dict_size = dict({'MenXS':'&size_id[]=206', 'MenS':'&size_id[]=207', 'MenM':'&size_id[]=208', 'MenL':'&size_id[]=209',\
'MenXL':'&size_id[]=210', 'MenXXL':'&size_id[]=211', 'MenXXXL':'&size_id[]=212', 'Men4XL':'&size_id[]=308',\
'Men5XL':'&size_id[]=309', 'Men6XL':'&size_id[]=1192', 'Men7XL':'&size_id[]=1193', 'Men8XL':'&size_id[]=1194',\
'Men38':'&size_id[]=776', 'Men39':'&size_id[]=778',\
'Men40':'&size_id[]=780', 'Men41':'&size_id[]=782', 'Men42':'&size_id[]=784',\
'Men42.5':'&size_id[]=785', 'Men43':'&size_id[]=786', 'Men43.5':'&size_id[]=787', 'Men44':'&size_id[]=788',\
'Men44.5':'&size_id[]=789', 'Men45':'&size_id[]=790', 'Men45.5':'&size_id[]=791', 'Men46':'&size_id[]=792',\
'Men47':'&size_id[]=794', 'Men48':'&size_id[]=1190', 'Men49':'&size_id[]=1191',\
'WomenXXXS':'&size_id[]=1226','WomenXXS':'&size_id[]=102',\
'WomenXS':'&size_id[]=2', 'WomenS':'&size_id[]=3', 'WomenM':'&size_id[]=4', 'WomenL':'&size_id[]=5',\
'WomenXL':'&size_id[]=6', 'WomenXXL':'&size_id[]=7', 'WomenXXXL':'&size_id[]=310', 'Women4XL':'&size_id[]=311',\
'Women5XL':'&size_id[]=312', 'Women6XL':'&size_id[]=1227', 'Women7XL':'&size_id[]=1228', 'Women8XL':'&size_id[]=1229',\

'Women35':'&size_id[]=55', 'Women35.5':'&size_id[]=1195',\
'Women36':'&size_id[]=56', 'Women36.5':'&size_id[]=1196', 'Women37':'&size_id[]=57',\
'Women37.5':'&size_id[]=1197', 'Women38':'&size_id[]=58', 'Women38.5':'&size_id[]=1198',\

'Women39':'&size_id[]=59', 'Women39.5':'&size_id[]=1199',\
'Women40':'&size_id[]=60', 'Women40.5':'&size_id[]=1200', 'Women41':'&size_id[]=61',\
'Women41.5':'&size_id[]=1201', 'Women42':'&size_id[]=62', 'Women43':'&size_id[]=62'})
dict_color = dict({'black':'&color_id[]=1', 'white':'&color_id[]=12', 'grey':'&color_id[]=3', \
'cream':'&color_id[]=20', 'beige':'&color_id[]=4', 'apricot':'&color_id[]=21', 'orange':'&color_id[]=11',\
'coral':'&color_id[]=22', 'red':'&color_id[]=7','burgundy':'&color_id[]=23','pink':'&color_id[]=5',\
'rose':'&color_id[]=24', 'purple':'&color_id[]=6', 'lila':'&color_id[]=25', 'light blue':'&color_id[]=26',\
'blue':'&color_id[]=9', 'navy blue':'&color_id[]=27', 'turquoise':'&color_id[]=17', 'mint':'&color_id[]=30',\
'green':'&color_id[]=10','dark green':'&color_id[]=28','khaki':'&color_id[]=16', 'brown':'&color_id[]=2',\
'mustard':'&color_id[]=29', 'yellow':'&color_id[]=8', 'silver':'&color_id[]=13', 'golden':'&color_id[]=14',\
'multicolor':'&color_id[]=15'})
dict_brand = dict({'nike':'&brand_id[]=53', 'adidas': '&brand_id[]=14', 'zara':'&brand_id[]=12', "levi's":'&brand_id[]=10',\
'h&m':'&brand_id[]=7', 'ralph lauren':'&brand_id[]=88', 'mango':'&brand_id[]=15', 'lacoste':'&brand_id[]=304', \
'calvin klein':'&brand_id[]=255', 'tommy hilfiger': '&brand_id[]=94', 'guess':'&brand_id[]=20', 'michael kors':'&brand_id[]=6005', \
'jordan':'&brand_id[]=2703', 'puma':'&brand_id[]=535', 'balenciaga':'&brand_id[]=2369', 'vans':'&brand_id[]=139'})
dict_condition = dict({'new with label':'&status[]=6', 'new': '&status[]=1', 'very good condition': '&status[]=2', \
'good condition':'&status[]=3', 'satisfactory':'&status[]=4'})

def define_criteria_string(order = [], catalog = [], size = [], color = [], brand = [], min_price = 'Na', max_price = 'Na', condition = []):
    # I - Create criteria string based on these dictionaries
    order_str = ''.join([dict_order[y] for y in order])
    catalog_str = ''.join([dict_catalog[y] for y in catalog])
    size_str = ''.join([dict_size[y] for y in size])
    color_str = ''.join([dict_color[y] for y in color])
    brand_str = ''.join([dict_brand[y] for y in brand])
    condition_str = ''.join([dict_condition[y] for y in condition])

    if min_price != 'Na':
        min_price_str = '&price_from={}'.format(min_price)
    else:
        min_price_str = ''

    if max_price != 'Na':
        max_price_str = '&price_to={}'.format(max_price)
    else:
        max_price_str = ''

    criteria_string = order_str + catalog_str + size_str + color_str + \
        brand_str + min_price_str + max_price_str + condition_str

    return(criteria_string)



def interactive_search():
    query = input("Which item do you want to research on vinted.fr ? \n")
    return(query)
def interactive_version():
    print(f'\n {Spy.vert}Maintenant quelques critères, vous pouvez en sauter en appuyant directement sur Entrée. {Spy.blanc}\n ')
    order_str = [
        input("Indiquez l'ordre de la recherche ( 1 choix maximum)parmis la liste suivante: \n {} \n".format(dict_order.keys()))]
    order_str = [element for item in order_str for element in item.split(',')]
    catalog_str = [input(
        "Indiquez le catalogue de recherche (1 choix maximum) parmis la liste suivante  \n {} \n".format(dict_catalog.keys()))]
    catalog_str = [element for item in catalog_str for element in item.split(',')]
    size_str = [
        input("Indiquez la taille pour la recherche (autant que vous voulez) parmis la liste suivante: \n {} \n".format(dict_size.keys()))]
    size_str = [element for item in size_str for element in item.split(',')]
    color_str = [input(
        "Indicatez des couleurs pour la recherche (2 choix maximum) parmi les choix suivants : \n {} \n".format(dict_color.keys()))]
    color_str = [element for item in color_str for element in item.split(',')]
    brand_str = [input(
        "Indicatez des marques pour la recherche (autant que vous voulez) parmi les choix suivants : \n {} \n".format(dict_brand.keys()))]
    brand_str = [element for item in brand_str for element in item.split(',')]
    condition_str = [input("Indicatez les conditions pour la recherche (5 max) parmi les choix suivants: \n {} \n".format(
        dict_condition.keys()))]
    condition_str = [element for item in condition_str for element in item.split(',')]

    min_price, max_price = 'Na', 'Na'
    min_price = input("Voulez vous un prix minimum ? ")
    max_price = input("Voulez-vous un prix maximum ? ")

    #end_page = input('Until which page do you want to collect data? (max = 400)')
    if order_str == ['']:
        order_str = []
    if catalog_str == ['']:
        catalog_str = []
    if size_str == ['']:
        size_str = []
    if color_str == ['']:
        color_str = []
    if brand_str == ['']:
        brand_str = []
    if condition_str == ['']:
        condition_str = []

    criteria_string = define_criteria_string(order=order_str, catalog=catalog_str, size=size_str, color=color_str, \
                                             brand=brand_str, min_price=min_price, max_price=max_price,
                                           condition=condition_str)
    return criteria_string



def get_page(criteria_string, query, count=1):
    pages = []
    base_url = "https://www.vinted.fr/catalog?search_text="
    query = query.replace(' ', '%20')
    for page_nb in range(1, count + 1):
        page_url = f"{base_url}{query}{criteria_string}&page={page_nb}"
        driver.get(page_url)

        if page_nb == 1:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.feed-grid__item')))

        pages.append(driver.page_source.encode("utf-8"))

    return pages


def get_info_on_page_2(pages):
    result = []

    for page_html in pages:
        soup = BeautifulSoup(page_html, "html.parser")
        articles = soup.find_all("div", class_="feed-grid__item")

        for article in articles:
            price = article.find("div", class_="title-content").text.strip()
            size = article.find("div", class_="new-item-box__description").text.strip()
            brand_element = article.find("p", attrs={"data-testid": "description-subtitle"})
            brand = brand_element.text.strip() if brand_element else "Marque non spécifiée"
            a_tag = article.find("a", class_="new-item-box__overlay")
            image_link = a_tag['href'].strip() if a_tag else None
            link_element = article.find('a',
                                        class_='new-item-box__overlay new-item-box__overlay--clickable new-item-box__overlay--gradient')
            link_product = link_element['href'] if link_element else None  # Handle cases where link is absent
            result.append(
                {f"Prix": price, f"Taille": size, f"Marque": brand,
                 f"Photo": image_link, f"Lien": link_product})

    df = pd.DataFrame(result)
    return df



def main():
    query = interactive_search()
    #criteria_string = interactive_version()
    criteria_string = define_criteria_string(order=["relevance"],catalog =["men"], )
    pages = get_page(criteria_string=criteria_string,query = query, count=1)
    data = get_info_on_page_2(pages)
    print(data)
    # Enregistrer la DataFrame dans un fichier CSV
    data.to_csv("vinted_data.csv", index=False)







