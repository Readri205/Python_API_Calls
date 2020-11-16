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


ENDPOINT = "https://trefle.io/api/v1/plants?"
YOUR_TREFLE_TOKEN = os.environ.get("YOUR_TREFLE_TOKEN")
PAGE_NUMBER = "&page=1"


ENDPOINT_SPECIES = "https://trefle.io/api/v1/species?"
FILTER = "&filter[flower_color]=red"
SEARCH = "&q=Sharon"

r = requests.get(
    f"{ENDPOINT}token={YOUR_TREFLE_TOKEN}{PAGE_NUMBER}")

species_filter = requests.get(
    f"{ENDPOINT_SPECIES}token={YOUR_TREFLE_TOKEN}{FILTER}")

plants = r.json()

searches = species_filter.json()

print(len(plants['data']))

# print(type(plants['data']))


for plant in plants['data']:
    name = plant['common_name']
    family = plant['family']
    family_common_name = plant['family_common_name']
    print(f"Name: {name}\tFamily: {family}\tFamily Common Name: {family_common_name}\n")


# print(species_filter)

@app.route("/")
@app.route("/get_plants")
def get_plants():
    plant = plants['data']
    return render_template("trefle_plants.html", plants=plant)


# print(plants)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
