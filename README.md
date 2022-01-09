# Electronic voting

## Installation

Ce programme fonctionne sur Python 3.8. Vous aurez besoin de pipenv, installable avec `pip3 install pipenv`.

Installez ensuite les dépendances du projet avec `pipenv install`. Entrez dans le venv avec `pipenv shell`.

Enfin, executez `cp .env.example .env` pour y mettre vos variables d'environnement. Vous pouvez le laisser tel quelle.

Vous pouvez désormais lancer le projet avec la commande `python3 src/main.py`.

Pour lancer un vote, la première étape sera de créer des electeurs et ensuite de créer une éléction.

A noter que les clés privées des utilisateurs sont actuellement stockées dans la base de donnée par soucis de confort. Le code ne les utilise néanmoins en aucun cas.
