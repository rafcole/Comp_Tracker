from flask import Flask, render_template
import requests
import json
from scraper import Scraper

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def idk():
    scraper = Scraper()
    scraper.log_in()
    return 'login'