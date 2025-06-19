import requests
from datetime import datetime
import dotenv

APP_ID = dotenv.get_key(dotenv_path=".env", key_to_get="APP_ID")
API_KEY = dotenv.get_key(dotenv_path=".env", key_to_get="API_KEY")
SHEETY_TOKEN = dotenv.get_key(dotenv_path=".env", key_to_get="SHEETY_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = dotenv.get_key(dotenv_path=".env", key_to_get="sheety_endpoint")

GENDER = "Male"
WEIGHT_KG = 55
HEIGHT_CM = 180
AGE = 21

exercise_text = input("Tell me which exercises you did: ")
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%H:%M:%S")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

bearer_headers = {
"Authorization": f"Bearer {SHEETY_TOKEN}"
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)
print(sheet_response.text)
