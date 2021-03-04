# -*- coding: utf-8 -*-
import requests
from apikey import KEY

# user_city = input("Write down a city name...  ").lower()

# data_current_weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_city}'
#                                     f'&appid={KEY}&units=metric').json()
data_onecall_api = requests.get(f'http://api.openweathermap.org/data/2.5/onecall?lat=4.449124&lon=41.449124'
                                f'&exclude=current,daily,alerts,minutely&appid={KEY}&units=metric').json()
weather_12_hours = [x['weather'][0]['main'] for x in data_onecall_api['hourly'][:24]]
print(weather_12_hours)
# if data_current_weather["cod"] != 200:
#     print(data_current_weather["message"])
# else:
#     print(f"Temp right now of {user_city} == {data_current_weather['main']['temp']}ºC")
