import os
import requests
import json
from flask import (
    Flask, render_template, url_for)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# @app.route("/")
# def hello():
#    return "Hello World ... again!"


ENDPOINT = "https://trefle.io/api/v1/plants/search?token="
YOUR_TREFLE_TOKEN = os.environ.get("YOUR_TREFLE_TOKEN")
PAGE_NUMBER = "&page=20"


ENDPOINT_SPECIES = "https://trefle.io/api/v1/species?"
FILTER = "&filter[common_name]=coconut%20palm"
STRG = "&q="
SEARCH = "rose of sharon"

r = requests.get(
    f"{ENDPOINT}{YOUR_TREFLE_TOKEN}{STRG}{SEARCH}")

species_filter = requests.get(
    f"{ENDPOINT_SPECIES}{YOUR_TREFLE_TOKEN}{FILTER}")

plants = r.json()

searches = species_filter.json()

# print(len(plants['data']))

# print(type(plants['data']))


for plant in plants['data']:
    plant_id = plant['id']
    name = plant['common_name']
    family = plant['family']
    family_common_name = plant['family_common_name']
    image = plant['image_url']
    links = plant['links']
    species = links['self']
    print(f"Plant ID: {plant_id}\tName: {name}\tFamily:{family}\tFamily Common Name:{family_common_name}\tImage: {image}")
    print(f"{species}\n")

links = plants['links']
first = links['first']
current = links['self']
last = links['last']
print(f"{current}\n{first}\n{next}\n{last}")

# print(species_filter)

@app.route("/")
@app.route("/get_trefle")
def get_trefle():
    plant = plants['data']
    return render_template("trefle_plants.html", plants=plant)


# print(plants)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
