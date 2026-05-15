import pandas as pd
from et0 import compute_et0

# Load merged weather data
df = pd.read_csv("../data_pipeline/merged_weather_data.csv")

# Compute ET0
df = compute_et0(df)

# Save output
df.to_csv("et0_output.csv", index=False)

# Preview results
print(df.head())
print(df["ET0"].describe())