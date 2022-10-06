import requests
import os
import datetime

os.system("pip install requests")
response = requests.get(
    "https://weather.lewagon.com/data/2.5/forecast?lat=51.5073219&lon=-0.1276474&units=metric").json()
# Do not modify the code above

london = {
    "city": {
        "name": "London"
    },
    "list": [
        {},
        {"weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
            }
        ],
            "dt_txt": str(datetime.date.today() + datetime.timedelta(days=1)) + " 06:00:00"
        }
    ]
}


def weather_forecast(london):
    city = london["city"]["name"]
    tomorrow = str(datetime.date.today() +
                   datetime.timedelta(days=1)) + " 06:00:00"

    for i in range(len(london.get("list"))):

        if len(london.get("list")[i]) == 0:
            print("test")
            continue

        if london.get("list")[i]["dt_txt"] == tomorrow:
            forecast = london.get("list")[i]["weather"][0]["main"]

    return f"The weather in {city} tomorrow is {forecast}"


print(weather_forecast(london))

response1 = requests.get(
    "https://weather.lewagon.com/data/2.5/forecast?lat=41.390205&lon=2.154007&units=metric").json()
print(weather_forecast(response1))
