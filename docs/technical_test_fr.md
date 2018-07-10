## Test technique pour développeur Python :

Créer une **API REST** avec [Flask](http://flask.pocoo.org/) capable de renvoyer pour les endpoints suivants :

##

**Search endpoint** :

***1.*** ```/recipes/search{keywords}/{limit}/{offset}?download```
 
Retourne une liste au format JSON des liens de chaque image principale des recettes
- Le paramètre `keywords` est composé d’un ou plusieurs mot-clés permettant une recherche parmis les recettes de Marmiton
- Les paramètres `offset` et `limit` autorise une pagination parmis les résultats
- Le paramètre `download ` est optionnel et permet le téléchargement de l’ensemble des images regroupées dans une archive zip.

##

**Database endpoints** :

***2.*** ```/recipes/add/{slug_recipe}```
Retourne le résultat d’une insertion correcte ou non de la recette dans un index Elasticsearch.
> Exemple : /favorites/add/recette_cookie-shot-facon-tarte-aux-fruits-rouges_354850

À l’appel de l’URL la recette doit être retrouvée et ajoutée dans Elasticsearch.

***3.*** ```/recipes```
Retourne la liste des recettes enregistrées via le endpoint précédent.

##

> Afin de faciliter les tests, l’utilisation de Docker est requise.

> Voici une librairie disponible pour les requêtes sur marmiton.org :
https://github.com/remaudcorentin-dev/python-marmiton
