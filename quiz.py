import json
import random

with open("countries_info.json", "r") as file:
    COUNTRIES = json.load(file)

COUNTRY = random.choice(COUNTRIES)
print(f"{COUNTRY['capital']} is the capital of {COUNTRY['name']['common']}.")
