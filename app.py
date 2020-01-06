from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
API_KEY_MAP = os.getenv("API_KEY_MAP")
API_KEY_GEO = os.getenv("API_KEY_GEO")


@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Home')

@app.route('/sun')
def sun():
    """Return Sunrise/Sunset Page"""
    city = request.args.get("search")
    if city == None:
        city = "San Francisco, CA"
    params = {
        'key': API_KEY_MAP,
        'location': city
        }
    r = requests.get('http://open.mapquestapi.com/geocoding/v1/address', params=params)
    lat = r.json()["results"][0]["locations"][0]["latLng"]["lat"]
    long = r.json()["results"][0]["locations"][0]["latLng"]["lng"]
    headers = {
        'apiKey': API_KEY_GEO,
        'lat': lat,
        'long': long
        }
    s = requests.get('https://api.ipgeolocation.io/astronomy', params=headers)
    sunrise = s.json()["sunrise"]
    sunset = s.json()["sunset"]
    return render_template('sun.html', sunrise=sunrise, sunset=sunset, city=city)

@app.route('/stars')
def stars():
    """Return Stars Page"""
    return render_template('stars.html')


if __name__ == '__main__':
    app.run(debug=True)
