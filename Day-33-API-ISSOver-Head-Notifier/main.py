import requests

reponse = requests.get('http://api.open-notify.org/iss-now.json').json()

latitude = reponse['iss_position']['latitude']
longitude = reponse['iss_position']['longitude']

iss_position = (latitude, longitude)
print(iss_position)

