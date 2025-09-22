import requests
from datetime import datetime
import os

GENDER = C_GENDER
WEIGHT_KG = C_WEIGHT_KG
HEIGHT_CM = C_HEIGHT_CM
AGE = C_AGE

APP_ID = os.environ["NT_APP_ID"] #NutriTionix
API_KEY = os.environ["NT_API_KEY"] #NutriTionix

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_params = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
data = response.json()

today = datetime.now()
formatted_today = today.strftime("%d/%m/%Y") #day/month/year
formatted_time = today.strftime("%X") #00:00


for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": formatted_today,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

### Basic Authentication - Sheety ###
sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(
      os.environ["USERNAME"], #Username
      os.environ["PASSWORD"], #Password
  )
)

print("Workout Saved")
