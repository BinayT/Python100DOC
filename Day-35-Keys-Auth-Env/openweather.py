# -*- coding: utf-8 -*-
import requests
from apikey import KEY, TWILIO_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client

data_onecall_api_params = {
    'lat': 39.215231,
    'lon': -8.072670,
    'appid': KEY,
    "units": 'metric',
    "exclude": 'current,daily,alerts,minutely'
}

# user_city = input("Write down a city name...  ").lower()

# data_current_weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_city}'
#                                     f'&appid={KEY}&units=metric').json()

data_onecall_api = requests.get(f'http://api.openweathermap.org/data/2.5/onecall', data_onecall_api_params).json()
weather_12_hours = [x['weather'][0]['main'] for x in data_onecall_api['hourly'][:48] if x['weather'][0]['id'] < 900]


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
if len(weather_12_hours) > 0:
    message = client.messages \
        .create(
        body="Trying Twilio.",
        from_='MyNumber',
        to='DestinationNumber'
    )

# if data_current_weather["cod"] != 200:
#     print(data_current_weather["message"])
# else:
#     print(f"Temp right now of {user_city} == {data_current_weather['main']['temp']}ºC")
