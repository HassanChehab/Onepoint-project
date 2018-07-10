## Technical test for Python developer :

Create an **REST API** with [Flask](http://flask.pocoo.org/) able to handle the followings endpoints :

##

**Search endpoint** :

***1.*** ```/recipes/search{keywords}/{limit}/{offset}?download```

Return a JSON list for each main pictures of recipes
- `keywords` parameter can be several keywords used for query the website
- `offset` and `limit` allow the response to be paginated
- `download` parameter is optional and return a ZIP archive containing main picture of each recipes

##

**Database endpoints** :

***2.*** ```/recipes/add/{slug_recipe}```
Return a successful or not response from an insertion of a recipe into Elasticsearch
> Example : /favorites/add/recette_cookie-shot-facon-tarte-aux-fruits-rouges_354850

When calling this URL, the recipe must be retrieve and inserted into Elasticsearch

***3.*** ```/recipes```
Return the recipes list previously saved

##

> In order to make tests easier, Docker must be used.

> Also you can use this available library for requesting marmiton.org 
https://github.com/remaudcorentin-dev/python-marmiton