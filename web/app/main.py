import re
import urllib3
import zipfile
from io import BytesIO
from datetime import datetime
from flask import Flask, url_for, jsonify, send_file

app = Flask(__name__)
http = urllib3.PoolManager()

# Create and send zip file with all marmitton images
def sendZipFile(marmittonUrls):
    file = open('./images.txt', 'w+')

    # create file
    for element in marmittonUrls:
        file.write(element + '\n')
    # Create zip file
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        zf.write('./images.txt')
    memory_file.seek(0)
    return send_file(memory_file, attachment_filename='data.zip', as_attachment=True)


# Set delemiter, return the list of searches
def getRecipesList(keywords):
    delemiter = ''
    recipesList = []

    if ';' in keywords:
        delemiter = ';'
    elif '|' in keywords:
        delemiter = '|'
    elif ' ' in keywords:
        delemiter = ' '
    elif ':' in keywords:
        delemiter = ':'

    if delemiter != '':
        recipesList = keywords.split(delemiter)
    else:
        recipesList.append(keywords)
    return recipesList


# Check if image is not already stored in list and append it if not
def addUrlsInList(marmittonUrls, tmp):
    for imageToFormat in tmp:
        formatedUrl = 'https://' + imageToFormat + '.jpg'
        if '.aspx' in imageToFormat:
            continue
        if formatedUrl in marmittonUrls:
            continue
        marmittonUrls.append(formatedUrl)
    return marmittonUrls


# This route get recipes from marimitton and allow user  to have pagination
@app.route('/recipes/search<string:keywords>/<int:limit>/<offset>', methods=['GET'])
def get_recipes(keywords, limit, offset):
    marmittonUrls = []
    recipesList = getRecipesList(keywords)

    for recipe in recipesList:
        marmittonResponse = http.request(
            'GET', 'https://www.marmiton.org/recettes/recherche.aspx?aqt=' + recipe)
        tmp = re.findall('https://(.*?).jpg', marmittonResponse.data)
        marmittonResponse = addUrlsInList(marmittonUrls, tmp)

    return sendZipFile(marmittonUrls)
    # return jsonify(marmittonUrls)

@app.route('/')
def index():
    return jsonify(status='ok', message='Hi there')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
