from re import I
import requests
import os
os.system("pip install requests")
response = requests.get(
    "https://weather.lewagon.com/geo/1.0/direct?q=london").json()


def city_info(response):
    dict = response[0]
    new_dict = {}
    new_dict['city'] = dict['name']
    new_dict['lat'] = dict['lat']
    new_dict['lon'] = dict['lon']
    return new_dict


x = list(city_info(response).keys())
print(x)
print(list(city_info(response).keys()) == ['city', 'lat', 'lon'])
