import requests
from credentials import *

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
print(response.text)

