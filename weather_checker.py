# -*- coding: utf-8 -*-
import requests
import json

api_key = "68a4a9c2eef038410098a962f513749c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter your city name: ")

full_url = "{}q={}&APPID={}".format(base_url,city_name,api_key)

response = requests.get(full_url)
x = response.json()


if x['cod'] == '404':
    print("City not found!!!!")
else:
    print("****************Weather report of {},{} *************".format(x['name'], x['sys']['country']) )
    max_temp = x['main']['temp_max'] - 273.15
    min_temp = x['main']['temp_min'] - 273.15
    for i in x['weather']:
        forecast = (i['description'])
    print("Forecast : {}".format(forecast))
    print("Maximum Temperature : {}°C".format(max_temp))
    print("Minimum Temperature : {}°C".format(min_temp))
    print("Humidity : {}".format(x['main']['humidity']))
    
