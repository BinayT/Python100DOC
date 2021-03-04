# -*- coding: utf-8 -*-
import requests
from apikey import KEY

user_city = input("Write down a city name...  ").lower()

data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={KEY}&units=metric').json()
if data["cod"] == '404':
    print(data["message"])
else:
    print(f"Temp right now of {user_city} == {data['main']['temp']}ºC")
