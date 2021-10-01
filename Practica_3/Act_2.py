import requests
import json
from datetime import datetime

# Numero 1
print("Numero 1:")
page = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall?lat=34.0430175&lon=-118.2672541&lang=es&units=metric&exclude=current,hourly,minutely,alerts&appid=b2d1fd8a7b6ce12cef92a0d03113461d"
)

weatherData = json.loads(page.content)

for x in range(0, 1):
    print("Datos generales")
    for elem in weatherData["daily"][x]:
        print(elem, ":\t", weatherData["daily"][x]["dt"])
    print(
        "dt",
        datetime.utcfromtimestamp(int(weatherData["daily"][x]["dt"])).strftime(
            "%d-%m-%Y %H:%M:%S"
        ),
    )

print("Numero 1:")
# Numero 2
page = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall?lat=34.0430175&lon=-118.2672541&lang=es&units=metric&exclude=current,hourly,minutely,alerts&appid=b2d1fd8a7b6ce12cef92a0d03113461d"
)
print("Temperaturas")
for x in range(0, 1):

    for mai in weatherData["daily"][x]["temp"]:
        print(mai, ":\t", weatherData["daily"][x]["temp"][mai])

print("Numero 3:")
# Numero 3
page = requests.get(
    "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/kimjiroshi?api_key=RGAPI-54b098b1-5870-4243-8304-281ceb82f20f"
)
print(page.status_code)
lol = json.loads(page.content)
for x, y in lol.items():
    print(x + ":", y)

print("Numero 4:")
# Numero 4
page = requests.get(
    "https://la1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=RGAPI-54b098b1-5870-4243-8304-281ceb82f20f"
)
print(page.status_code)

lol = json.loads(page.content)
for x, y in lol.items():
    print(x + ":", y)

print("Numero 5:")
# Numero 5
page = requests.get(
    "https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/X_2GTK1ySpnZ9gtZXt32Chh7Sc7S4OKL-cgE4omFTD5XLg?api_key=RGAPI-54b098b1-5870-4243-8304-281ceb82f20f"
)
print(page.status_code)
lol = json.loads(page.content)
print(page.content)
