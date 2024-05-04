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

@app.route("/event/<event_name>")
def get_event_info(event_name=None):
    scraper = Scraper()
    scraper.log_in()
    return scraper.get_event_details(event_name)