import requests
import datetime
APP_KEY = ''
APP_ID = ''
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

question = input("What exercise you did today?")

post_exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

post_exercise_params = {
    "query": question,
    "age": ,
    "gender": "",
    "height_cm": ,
    "weight_kg":
}

make_request = requests.post(url=nutritionix_endpoint, json=post_exercise_params, headers=post_exercise_headers)
print(make_request.text)
