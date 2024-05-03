from flask import Flask, render_template
import requests
import json
from scraper import login

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def idk():
    login("rio-salado-black-rifle-may-2024-2")
    return 'login'