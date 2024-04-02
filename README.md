Outil de recherche automatique d'articles Vinted
Objectif:
Ce projet vise à simplifier les recherches fastidieuses sur Vinted en automatisant la quête d'articles correspondant à vos critères spécifiques. Il vous envoie ensuite les informations pertinentes par email.

Fonctionnement:
Définissez vos préférences : Précisez le nom, la marque, la taille, la couleur et d'autres caractéristiques de l'article recherché. Vous avez également la possibilité de définir le nombre de pages Vinted à explorer.

Lancez le bot : Une fois vos préférences configurées, le bot se charge de parcourir les pages de Vinted et d'extraire les liens de tous les articles correspondant à vos critères.

Collectez les informations : L'outil récupère ensuite toutes les informations utiles de chaque article, telles que le prix, la description, les photos, et les stocke pour une consultation ultérieure.

Restez informé : Vous recevez un récapitulatif par email contenant les informations des derniers produits ajoutés, avec un lien vers chaque article pour une consultation facile.

Structure du code:
Le code est divisé en 5 modules distincts pour une meilleure organisation et une maintenance aisée:

Get_Link : Cette partie définit les caractéristiques de l'article recherché, explore un nombre défini de pages Vinted, extrait les liens de tous les articles présents et les stocke dans une base de données CSV.

Final_db : Elle itère sur chaque lien de la base de données CSV, collecte toutes les informations du produit grâce à BeautifulSoup et enrichit la base de données avec ces informations.

Get_Last : Trie les articles par date de publication et ne conserve que les X derniers articles définis par l'utilisateur.

Send_Mail : Envoie un email au propriétaire du bot avec les informations des X derniers produits ajoutés, incluant un lien vers chaque article.

Test : Cette partie permet d'exécuter automatiquement et en continu le bot en concaténant toutes les fonctions dans une boucle while.

Prérequis:
Python 3
Modules Selenium et BeautifulSoup
Un compte Vinted
Utilisation:
Installez les modules Selenium et BeautifulSoup.
Modifiez les paramètres de recherche dans la fonction Get_Link.
Lancez le script Python.
Remarques:
Le nombre de pages à scraper est limité par Vinted.
Veuillez respecter les conditions d'utilisation de Vinted.
Licence:
Ce projet est distribué sous licence MIT.

Contact:
N'hésitez pas à me contacter si vous avez des questions ou des suggestions.






