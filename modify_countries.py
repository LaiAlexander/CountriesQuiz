import json

with open("countries.json", "r") as file:
    COUNTRIES = json.load(file)

with open("countries_info.json", "w") as file:
    country_list = []
    for country in COUNTRIES:
        country_stripped = {}
        country_stripped["name"] = {}
        country_stripped["name"]["common"] = country["name"]["common"]
        country_stripped["name"]["official"] = country["name"]["official"]
        country_stripped["capital"] = country["capital"]
        country_stripped["region"] = country["region"]
        country_stripped["subregion"] = country["subregion"]
        country_list.append(country_stripped)
    json.dump(country_list, file, indent=4)
