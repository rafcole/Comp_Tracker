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
    scraper.quit()
    return 'login'

@app.route("/event/<event_name>", methods=['GET'])
def get_event_info(event_name=None):
    scraper = Scraper()
    scraper.log_in()
    details = scraper.get_event_details(event_name)
    scraper.quit()
    return details

@app.route("/club/<club_name>", methods=['GET'])
def get_events_from_club(club_name=None):
    scraper = Scraper()
    scraper.get_events_from_club(club_name)
    return 'okiedokie'