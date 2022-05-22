import requests, os
from datetime import datetime
from random import randint

GENDER = 'female'
WEIGHT_KG = randint(60, 80)
HEIGHT_CM = randint(155, 165)
AGE = randint(25, 35)

NUTRITIONIX_ID = 'secret'
NUTRITIONIX_KEY = 'secret'

headers = {
    'x-api-id': NUTRITIONIX_ID,
    'x-app-key': NUTRITIONIX_KEY,
    'Content-Type': 'application/json'
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_params = {
    'query': input('What exercise did you do today?: '),
    'gender': GENDER,
    'age': AGE,
    'weight': WEIGHT_KG,
    'height': HEIGHT_CM
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

add_row_endpoint = 'secret'
today = datetime.now()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(add_row_endpoint, json=sheet_inputs)
    print(sheet_response.text)
