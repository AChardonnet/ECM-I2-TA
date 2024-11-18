# Projet Web

Ce dépôt contient mon rendu pour le travail en autonomie.

## Initialisation

 1. Création de la base de données

`python manage.py migrate`

 2. Création d'un super utilisateur

`python manage.py createsuperuser`

 3. Importation de la base de données

`python manage.py loaddata fixtures/playground.json --app playground`

`python manage.py loaddata fixtures/blog.json --app blog`
