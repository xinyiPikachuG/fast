from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY") 

class WeatherRequest(BaseModel):
    city: str

@app.get("/")
def home():
    return {"message": "Welcome to the Weather Microservice! Use /weather to fetch weather data."}

@app.post("/weather")
def get_weather(data: WeatherRequest):
    city_query = data.city



    params = {
        "q": city_query,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data.")

    weather_data = response.json()

    return {
        "city": weather_data.get("name"),
        "temperature": weather_data["main"].get("temp"),
        "description": weather_data["weather"][0].get("description"),
        "humidity": weather_data["main"].get("humidity"),
        "wind_speed": weather_data["wind"].get("speed")
    }


