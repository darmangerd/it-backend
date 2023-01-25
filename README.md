# Projet application web - it

- David Darmanger
- 24.01.2023
- He-Arc

## Description

Site web permettant de gérer son alimentation facilement et rapidement en listant les aliments et leurs nutriments. De plus, il est possible d'avoir un historique de ses repas et de ses aliments, et plus encore. Pour plus d'informations voir le [cahier des charges](https://gitlab-etu.ing.he-arc.ch/groups/isc/2022-23/niveau-3/3298.4-developpement-web/it/-/wikis/Spécifications-détaillées) qui décrit le projet en détail.

## Installation

### Prérequis

#### Backend

- [Python 3.10.6](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

#### Frontend

- [Node.js](https://nodejs.org/en/)

### Lancer le backend

1. Cloner le projet backend

```sh
git clone git@gitlab-etu.ing.he-arc.ch:isc/2022-23/niveau-3/3298.4-developpement-web/it/backend.git
```

2. Activer l'environnement virtuel

```sh
cd backend
pipenv shell
pipenv install
pipenv install --dev
```

3. Créer la base de données

```sh
cd mysite/
python manage.py migrate
```

4. Lancer le serveur

```sh
python manage.py runserver
```

### Lancer le frontend

1. Cloner le projet frontend

```sh
git clone git@gitlab-etu.ing.he-arc.ch:isc/2022-23/niveau-3/3298.4-developpement-web/it/frontend.git
```

2. Installer les dépendances

```sh
cd frontend/it/
npm install
```

3. Lancer le serveur (depuis le dossier frontend/it/)

```sh
npm run dev
```

4. Accéder au site web

```sh
http://127.0.0.1:5173/
```

## Guide du projet

1. Il faut d'abord créer un compte utilisateur via l'interface de connexion.
2. Une fois connecté, il est possible de créer des aliments, des repas, et de les ajouter à l'historique.
3. D'abord, il faut créer un ou plusieurs aliments. Pour cela, il faut cliquer sur le bouton "Add a food" dans la barre de navigation. Une fois sur la page, il faut remplir les champs et cliquer sur "Add".
4. Ensuite depuis la page principale, il faut sélectionner la date puis un aliment dans la liste déroulante. Une fois l'aliment sélectionné, on entre la quantité et on clic sur le bouton d'ajout. Cela ajoute l'aliment au repas de la date sélectionnée.
5. Le graphique de compte des aliments est mis à jour automatiquement et le compte des calories/macro-nutriments est mis à jour en temps réel.
6. Il est possible de supprimer un aliment du repas en cliquant sur le bouton de supression à côté de l'aliment dans le repas.
7. Il est possible de modifier la quantité d'un aliment en entrant la modification dans le champ de quantité. La mise à jour se fait automatiquement.
8. Pour se déconnecter, il faut cliquer sur le bouton "Logout" dans la barre de navigation.

## Documentation

- Documentation du projet : [Wiki](https://gitlab-etu.ing.he-arc.ch/groups/isc/2022-23/niveau-3/3298.4-developpement-web/it/-/wikis/home)
- Documentation Swagger : `http://127.0.0.1:8000/swagger/`

## Administration backend

- Accéder à l'interface d'administration : `http://127.0.0.1:8000/admin/`

Créer un super utilisateur. Il ne devra être utilisé que pour la création de compte administrateur et non sur le site web.

```sh
cd mysite/
python manage.py createsuperuser
```
