import pandas as pd
from et0 import compute_et0

# Load forecast weather data
df = pd.read_csv("../ml_model/forecast_weather.csv")

# Compute ET0
df = compute_et0(df)

# Save output
df.to_csv("forecast_et0_output.csv", index=False)

print(df.head())
print("Future ET0 computed successfully!")