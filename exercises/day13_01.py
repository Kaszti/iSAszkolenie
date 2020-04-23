from flask import Flask, render_template, request, url_for
import day8_02 as downloader
import day8_03_02 as email
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def starter():
    return render_template('pobieraczek.html')

@app.route('/form', methods=['POST'])
def form():
    try:
        typ = request.form['typ']
    except:
        typ = 'obrazy'
    url_adress = request.form['url']
    email_adress = request.form['email']
    if typ == 'obrazy':
        files = downloader.picture_download(url_adress)
        #email.email_send(email_adress, files)
    elif typ == 'dokumenty':
        docs = downloader.documents_download(url_adress)
        if '.pdf' in docs:
            pass


        #email.email_send(email_adress, files)
    return render_template('pobieraczek.html', files_list = files)



app.debug = True
app.run()