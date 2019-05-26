import json
import random

with open("countries_info.json", "r") as file:
    COUNTRIES = json.load(file)

# reg = []
# for country in COUNTRIES:
#     if country['region'] not in reg:
#         reg.append(country['region'])

# regions = {}
# for r in reg:
#     regions[r] = []
# for country in COUNTRIES:
#     regions[country['region']].append(country)

# REGIONS = {}
# for country in COUNTRIES:
#     if country['region'] in REGIONS:
#         REGIONS[country['region']].append(country)
#     else:
#         REGIONS[country['region']] = []
#         REGIONS[country['region']].append(country)

REGIONS = {}
for country in COUNTRIES:
    if country['region'] in REGIONS:
        if country['subregion'] in REGIONS[country['region']]:
            REGIONS[country['region']][country['subregion']].append(country)
        else:
            REGIONS[country['region']][country['subregion']] = []
            REGIONS[country['region']][country['subregion']].append(country)
    else:
        REGIONS[country['region']] = {}
        REGIONS[country['region']][country['subregion']] = []
        REGIONS[country['region']][country['subregion']].append(country)


def main():
    play = True
    while play:
        region = random.choice(list(REGIONS))
        subregion = random.choice(list(REGIONS[region]))
        country = random.choice(REGIONS[region][subregion])
        capital = country['capital'].copy()
        country_name = country['name']['common']
        print(country)
        while capital:
            # print(country['capital'])
            if not capital[0]:
                break
            hint = list(capital[0])
            user_guess = input(f"What is the capital of {country_name}? ")
            if user_guess in capital:
                print("That's correct!")
                capital.remove(user_guess)
            elif user_guess == "pass":
                print(f"{capital} was the right answer.")
                break
            elif user_guess == "q":
                play = False
                break
            else:
                print("That's wrong.")
                print(f"Here's a hint: {('').join(hint[0:1])}")
            print(capital, flush=True)
            if (capital):
                print("Capital not empty.", flush=True)

if __name__ == "__main__":
    main()