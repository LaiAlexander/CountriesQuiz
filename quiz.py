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

REGIONS = {}
for country in COUNTRIES:
    if country['region'] in REGIONS:
        REGIONS[country['region']].append(country)
    else:
        REGIONS[country['region']] = []
        REGIONS[country['region']].append(country)


def main():
    play = True
    while play:
        country = random.choice(REGIONS[random.choice(list(REGIONS))])
        while country['capital']:
            hint = list(country['capital'][0])
            user_guess = input(f"What is the capital of {country['name']['common']}? ")
            if user_guess in country['capital']:
                print("That's correct!")
                country['capital'].remove(user_guess)
            elif user_guess == "pass":
                print(f"{country['capital']} was the right answer.")
                break
            elif user_guess == "q":
                play = False
                break
            else:
                print("That's wrong.")
                print(f"Here's a hint: {('').join(hint[0:1])}")

if __name__ == "__main__":
    main()