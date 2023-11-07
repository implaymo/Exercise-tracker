import requests
from dotenv import load_dotenv
import os
def configure():
    load_dotenv()

configure()

APP_ID = os.getenv("APP_ID")
APP_KEY= os.getenv("APP_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


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

response = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=exercise_data)
response.raise_for_status()

data = response.json()
print(data)