import requests
from bs4 import BeautifulSoup

ENDPOINT = "https://www.johnlewis.com/john-lewis-partners-murray-ergonomic-office-chair-black/p1919328"

response = requests.get(f"{ENDPOINT}")
google = response.content
soup = BeautifulSoup(google, "html.parser")
element = soup.find("p", {"class":"price price--large"})

string_price = element.text.strip()

price_without_symbol = string_price[1:]

price_as_float = float(price_without_symbol)

if price_as_float <= 300:
    print(f"Buy the chair for £{price_as_float}!")
else:
    print("Do not buy the chair!")

# <p class="price price--large">£250.00 </p>