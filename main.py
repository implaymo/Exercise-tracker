import requests
from dotenv import load_dotenv
import os
from datetime import datetime
def configure():
    load_dotenv()

configure()

APP_ID = os.getenv("APP_ID")
APP_KEY= os.getenv("APP_KEY")
MY_EMAIL = os.getenv("MY_EMAIL")
EXERCISE_ENDPOINT = os.getenv("EXERCISE_ENDPOINT")
POST_ENDPOINT = os.getenv("POST_ENDPOINT")

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

# Nutritionix.com Exercise Enpoint
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote_user-id": "0",
}
exercise_input = input("Which exercise have you done? ")
exercise_data = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 63.0,
    "height_cm": 170.0,
    "age": 26,
}

response_nutri = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=exercise_data)
response_nutri.raise_for_status()

data = response_nutri.json()


# Sheety.com Endpoint
for exercise in data:

data_for_sheet = {
    "sheet1":
        {
            "date": today_date,
            "time": time,
            "exercise": data["exercises"][0]["user_input"],
            "duration": data["exercises"][0]["duration_min"],
            "calories": data["exercises"][0]["nf_calories"]

        }
}

response_sheety = requests.post(url=POST_ENDPOINT, json=data_for_sheet, headers=headers)
response_sheety.raise_for_status()
