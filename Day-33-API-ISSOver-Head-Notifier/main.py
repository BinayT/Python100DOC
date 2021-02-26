import requests
BARCELONA_LAT = 41.385063
BARCELONA_LONG = 2.173404
# reponse = requests.get('http://api.open-notify.org/iss-now.json').json()
#
# latitude = reponse['iss_position']['latitude']
# longitude = reponse['iss_position']['longitude']
#
# iss_position = (latitude, longitude)

# https://api.sunrise-sunset.org/json

barcelona_sunset_sunrise_params = {
    "lat": BARCELONA_LAT,
    "lng": BARCELONA_LONG
}

sun_sunset_sunrise_apicall = requests.get(f'https://api.sunrise-sunset.org/json', params=barcelona_sunset_sunrise_params)
sun_sunset_sunrise_apicall_res = sun_sunset_sunrise_apicall.json()
sun_sunset_sunrise_apicall.raise_for_status()
print(sun_sunset_sunrise_apicall_res)

