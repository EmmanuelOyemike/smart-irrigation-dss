import requests
import pandas as pd
import sys

API_KEY = "d7c1eec060ad8bf1546f228b7dd5bc0b"


city = sys.argv[1]
fetch_forecast(city)

def fetch_forecast(city):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

forecast_data = []

for item in data["list"]:

    # Weather variables
    temp = item["main"]["temp"]
    humidity = item["main"]["humidity"]
    wind = item["wind"]["speed"]

    # Rainfall
    rainfall = item.get("rain", {}).get("3h", 0)

    # Cloud cover
    cloud_cover = item["clouds"]["all"]

    # Estimated solar radiation
    estimated_radiation = 25 * (1 - cloud_cover / 100)

    # Save everything
    forecast_data.append({
        "temp": temp,
        "humidity": humidity,
        "wind": wind,
        "rainfall": rainfall,
        "radiation": estimated_radiation,
        "date": item["dt_txt"]
    })

df = pd.DataFrame(forecast_data)

print(df.head())

df.to_csv("forecast_weather.csv", index=False)

print("Forecast saved!")

#Run Script
city = sys.argv[1]
fetch_forecast(city)