import requests
import pandas as pd

# Location (Kano, Nigeria)
LAT = 11.8500
LON = 8.6667

START = "20250101"
END = "20251231"

url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,RH2M,WS2M,ALLSKY_SFC_SW_DWN&community=AG&longitude={LON}&latitude={LAT}&start={START}&end={END}&format=JSON"

response = requests.get(url)
data = response.json()

# Extract variables
params = data["properties"]["parameter"]

df = pd.DataFrame({
    "date": list(params["T2M"].keys()),
    "temp": list(params["T2M"].values()),
    "humidity": list(params["RH2M"].values()),
    "wind": list(params["WS2M"].values()),
    "radiation": list(params["ALLSKY_SFC_SW_DWN"].values())
})

df.to_csv("weather_data.csv", index=False)

print("Weather data saved!")