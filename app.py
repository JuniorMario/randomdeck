#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import url_for
from card import card_it
__author__ = "JuniorMario"

app = Flask(__name__)

@app.route('/')
def index():
    deck = card_it()
    decky = card_it()

    return render_template('index.html', cartas=deck, cartas2=decky)

if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")
