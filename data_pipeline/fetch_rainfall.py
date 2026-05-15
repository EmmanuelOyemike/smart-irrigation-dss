import requests
import pandas as pd

LAT = 11.8500
LON = 8.6667

url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOT&community=AG&longitude={LON}&latitude={LAT}&start=20250101&end=20251231&format=JSON"

response = requests.get(url)
data = response.json()

print("DEBUG RESPONSE:", data)

if "properties" not in data:
    print("API ERROR:", data)
    exit()

params = data["properties"]["parameter"]

df = pd.DataFrame({
    "date": list(params["PRECTOTCORR"].keys()),
    "rainfall": list(params["PRECTOTCORR"].values())
})

print(df.head())

df.to_csv("rainfall_data.csv", index=False)

print("Rainfall data saved!")