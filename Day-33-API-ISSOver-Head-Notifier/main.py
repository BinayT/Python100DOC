import requests

reponse = requests.get('http://api.open-notify.org/iss-now.json').json()

latitude = reponse['iss_position']['latitude']
longitude = reponse['iss_position']['longitude']

iss_position = (latitude, longitude)

# https://api.sunrise-sunset.org/json

sun_setrise_apicall = requests.get(f'https://api.sunrise-sunset.org/json?lat={iss_position[0]}'
                                    f'&lng={iss_position[1]}')
sun_setrise_apicall_res = sun_setrise_apicall.json()
sun_setrise_apicall.raise_for_status()
print(sun_setrise_apicall_res)

