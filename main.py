import requests
from credentials import *
from datetime import datetime


GENDER = "male"
WEIGHT = 79.8
HEIGHT = 173.64
AGE = 30

#TODO 1: SET API ID and KEY
#Added from credentials file

#TODO 2: Use Nutronix NL for exercise API Docs to print stats for a plain text input
NUTRONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': NUTRONIX_API_ID,
    'x-app-key': NUTRONIX_API_KEYS,
    'Content-Type': 'application/json'
}

exercise = input("What exercise did you do today?: ")

request_body = {
 "query": exercise,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url=NUTRONIX_API_ENDPOINT, headers=headers, json=request_body)
result = response.json()
print(result)

##SHEETY SETUP
SHEETY_GOOGLE_SHEETS_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEETY_NAME}"

today_date = datetime.now().strftime("%d%m%Y")
today_time = datetime.now().strftime("%X")

workout_data = result["exercises"]

for workout in workout_data:
    sheety_parameters = {
        "workouts": {
            "date": today_date,
            "time": today_time,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }

    }

sheety_response = requests.post(url=SHEETY_GOOGLE_SHEETS_ENDPOINT, json=sheety_parameters)

print(sheety_response.text)

