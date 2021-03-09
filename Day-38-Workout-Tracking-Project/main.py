import requests
import datetime
APP_KEY = ''
APP_ID = ''
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_post_endpoint = 'https://api.sheety.co/28b51b82d298a761f7348503bed09834/myWorkouts/workouts'

question = input("What exercise you did today?")

post_exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

post_exercise_params = {
    "query": question,
    "age": 25,
    "gender": "male",
    "height_cm": 175,
    "weight_kg": 76
}

date_today = datetime.datetime.now().strftime('%d/%m/%Y')
current_time = datetime.datetime.now().strftime('%H:%M:%S')

# TODO 1: First post to the nutritionix API and get the value back from it.
post_to_nutritionix = requests.post(url=nutritionix_endpoint, headers=post_exercise_headers, json=post_exercise_params)
response_from_nutritionix = post_to_nutritionix.json()
# exercise_name = exercises.user_input, duration = exercises.duration_min, calories = exercises.nf_calories

sheety_headers = {
    "Authorization": ""
}

for exercises in response_from_nutritionix['exercises']:
    print(exercises['user_input'])
    sheety_params = {
        'workout': {
            "date": str(date_today),
            "time": str(current_time),
            "exercise": exercises['user_input'],
            "duration": exercises['duration_min'],
            "calories": exercises['nf_calories']
        }
    }
    post_to_google_sheets = requests.post(
        url="https://api.sheety.co/28b51b82d298a761f7348503bed09834/myWorkouts/workouts",
        headers=sheety_headers,
        json=sheety_params)
    print(post_to_google_sheets.text)