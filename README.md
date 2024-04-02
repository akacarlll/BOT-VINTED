# BOT-VINTED

<details>
<summary><strong>ℹ️ Important</strong></summary>

Ce script Python utilise Selenium pour surveiller les nouvelles annonces sur Vinted répondant à certains critères et envoie des notifications par e-mail lorsque de telles annonces sont trouvées.

</details>


Ce script Python utilise Selenium pour surveiller les nouvelles annonces sur Vinted répondant à certains critères et envoie des notifications par e-mail lorsque de telles annonces sont trouvées.

## Fonctionnalités principales :
Surveillance Automatisée : Le bot scrute périodiquement les nouvelles annonces sur Vinted en fonction des critères définis.
Notification par E-mail : Lorsqu'une nouvelle annonce est détectée, le bot envoie une notification par e-mail avec des détails sur l'annonce.
Critères de Recherche Personnalisables : Les critères de recherche tels que le produit recherché, le prix maximum et la taille sont facilement ajustables.
Intégration avec SendGrid : Les notifications par e-mail sont envoyées via l'API SendGrid.

## Prérequis :
Avant d'exécuter le script, assurez-vous d'avoir les éléments suivants installés :

Python (version 3.x)
Selenium (pip install selenium)
SendGrid (pip install sendgrid)
Navigateur Web compatible avec Selenium (par exemple, Google Chrome)
Navigateur Web compatible avec Selenium (par exemple, Google Chrome)
Webdriver Chrome (Téléchargeable depuis https://chromedriver.chromium.org/downloads et doit être placé dans le PATH ou dans le même répertoire que le script)

## Configuration :
Avant de lancer le script, vous devez effectuer les configurations suivantes dans le fichier Python :

Définissez les variables RECHERCHE, MAX_PRIX, MAX_SIZE_ELEMENT, TO_EMAIL et SENDER_MAIL selon vos préférences.
Assurez-vous que la variable URL est correctement configurée pour la recherche sur Vinted.

## Utilisation :
Exécutez le script Python en utilisant la commande python nom_du_script.py.
Le script commencera à surveiller les nouvelles annonces sur Vinted.
Lorsqu'une nouvelle annonce correspondant aux critères est trouvée, une notification par e-mail sera envoyée à l'adresse spécifiée.

## Améliorations Possibles :
Ajouter la prise en charge d'autres méthodes de notification, telles que les notifications push sur mobile.
Permettre une configuration plus avancée des critères de recherche, par exemple en ajoutant des filtres supplémentaires.
Implémenter une interface utilisateur pour faciliter la configuration et la surveillance des annonces.
Assurez-vous de bien comprendre le code et les configurations avant de l'exécuter. Si vous avez des questions ou des suggestions d'amélioration, n'hésitez pas à les mentionner dans les commentaires du script ou à les ajouter à ce README.
