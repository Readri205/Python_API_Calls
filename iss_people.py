import requests

ENDPOINT = "http://api.open-notify.org/astros.json"

response = requests.get(f"{ENDPOINT}")

astronaut_name = response.json()

print(astronaut_name['number'])
print(astronaut_name['people'])

for p in astronaut_name['people']:
    print(p['name'])
