import os
import requests
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["YOUR_TREFLE_TOKEN"] = os.environ.get("YOUR_TREFLE_TOKEN")


@app.route("/")
def hello():
    return "Hello World ... again!"


ENDPOINT = "https://trefle.io/api/v1/plants/search?"
YOUR_TREFLE_TOKEN = ""
PAGE_NUMBER = "&page=1"


ENDPOINT_SPECIES = "https://trefle.io/api/v1/species?"
FILTER = "&filter[flower_color]=red"
SEARCH = "&q=Solanaceae"

r = requests.get(
    f"{ENDPOINT}token={YOUR_TREFLE_TOKEN}{SEARCH}")

species_filter = requests.get(
    f"{ENDPOINT_SPECIES}token={YOUR_TREFLE_TOKEN}{FILTER}")

plants = r.json()

searches = species_filter.json()

# print(plants)

# print(species_filter)

# for plant in plants['data']:
#   print(plant['common_name'])

# print(plants)

for i in plants['data']:
    print(i['common_name'])
    print(i['id'])
    print(i['family_common_name'])
#   print(i['image_url'])


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
