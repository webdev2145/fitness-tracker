import requests
from credentials import *

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
 "query": f"{exercise}",
 "gender": "male",
 "weight_kg": 79.8,
 "height_cm": 173.64,
 "age": 30
}

response = requests.post(url=NUTRONIX_API_ENDPOINT, headers=headers, json=request_body)
print(response.text)

