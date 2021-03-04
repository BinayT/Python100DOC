# -*- coding: utf-8 -*-
import requests
from apikey import KEY

user_city = input("Write down a city name...  ").lower()

data_current_weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_city}'
                                    f'&appid={KEY}&units=metric').json()
data_onecall_api = requests.get(f'http://api.openweathermap.org/data/2.5/onecall?lat=41.449124&lon=41.449124'
                                f'&exclude=hourly,daily&appid={KEY}&units=metric').json()
print(data_onecall_api)
# if data_current_weather["cod"] != 200:
#     print(data_current_weather["message"])
# else:
#     print(f"Temp right now of {user_city} == {data_current_weather['main']['temp']}ºC")
