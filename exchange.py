import requests

APP_ID = "6eb0b4306e5f4128bb097b0eddf71dd0"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']
zar_amount = usd_amount * exchange_rates['rates']['ZAR']
eur_amount = gbp_amount * exchange_rates['rates']['EUR']
gbp_amount = round(gbp_amount, 2)
zar_amount = round(zar_amount, 2)
eur_amount = round(eur_amount, 2)

gbp_inverse = round(usd_amount / gbp_amount, 2)
gbp_usd = gbp_inverse * usd_amount
gbp_zar = round(zar_amount * gbp_inverse, 2)
gbp_eur = round(eur_amount * gbp_inverse, 2)

print(f"Base Currency:\t{exchange_rates['base']}\tSet at US${usd_amount}")

print(f"US$\t{usd_amount} is GBP\t{gbp_amount}")
print(f"US$\t{usd_amount} is ZAR\t{zar_amount}")
print(f"US$\t{usd_amount} is EUR\t{eur_amount}")
print(f"GBP\t{usd_amount} is US$\t{gbp_usd}")
print(f"GBP\t{usd_amount} is ZAR\t{gbp_zar}")
print(f"GBP\t{usd_amount} is EUR\t{gbp_eur}")
