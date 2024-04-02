# BOT-VINTED
Ce projet consiste en un bot Python conçu pour surveiller les nouveaux articles sur le site Vinted et notifier l'utilisateur lorsque des articles répondant à certains critères sont trouvés. Le bot utilise l'automatisation du navigateur avec Selenium pour naviguer sur le site, extraire les informations sur les articles et envoyer des notifications par e-mail à l'utilisateur.

## Fonctionnalités
Recherche automatique de nouveaux articles sur Vinted en fonction de critères définis (par exemple, marque, prix, taille, etc.).
Notification par e-mail lorsqu'un nouvel article correspondant aux critères est trouvé.
Possibilité de définir des critères de recherche personnalisés, tels que la marque, la taille, le prix, etc.
Utilisation de l'automatisation du navigateur avec Selenium pour simuler le comportement de l'utilisateur sur le site Vinted.

## Configuration
Avant d'utiliser le bot, vous devez configurer certains paramètres :

Critères de recherche : Définissez les critères de recherche en modifiant les variables telles que RECHERCHE, MAX_PRIX, etc. dans le code Python.

Adresse e-mail : Configurez l'adresse e-mail de l'utilisateur dans la variable TO_EMAIL pour recevoir les notifications.

Compte SendGrid (facultatif) : Si vous utilisez SendGrid pour envoyer des e-mails, configurez votre API SendGrid dans le code Python.

Navigateur Web : Assurez-vous d'avoir le navigateur Chrome installé sur votre système, ainsi que le pilote Chrome WebDriver approprié.

## Installation
Cloner ce dépôt sur votre machine locale.

Assurez-vous d'avoir Python installé sur votre système.

Installez les dépendances requises en exécutant pip install -r requirements.txt.

Configurez les paramètres nécessaires dans le fichier Python.

Exécutez le fichier Python avec python bot_vinted.py.

## Exigences
Python 3.x
Selenium
SendGrid (facultatif)
Navigateur Chrome et pilote Chrome WebDriver
Limitations
Le bot peut ne pas être efficace si le site Vinted met en place des mesures de protection contre les bots, comme des CAPTCHA ou des restrictions de débit.
Les modifications ultérieures du site Vinted peuvent nécessiter des ajustements dans le code pour maintenir le bon fonctionnement du bot.
Contribution
Les contributions sont les bienvenues ! Si vous trouvez des bugs ou si vous souhaitez ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une issue ou à proposer une pull request.

## Avertissement
Ce projet a été réalisé à des fins éducatives et de démonstration uniquement. L'utilisation de ce bot pour collecter des données à grande échelle ou pour tout autre but contraire aux conditions d'utilisation de Vinted est strictement interdite. Utilisez-le à vos propres risques.
