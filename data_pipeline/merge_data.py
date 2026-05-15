import pandas as pd

# Load datasets
weather_df = pd.read_csv("weather_data.csv")
rain_df = pd.read_csv("rainfall_data.csv")

# Convert dates
weather_df["date"] = pd.to_datetime(weather_df["date"], format="%Y%m%d")
rain_df["date"] = pd.to_datetime(rain_df["date"], format="%Y%m%d")

# Merge datasets
df = pd.merge(weather_df, rain_df, on="date", how="inner")

# Clean missing values
df.replace(-999, None, inplace=True)
df.dropna(inplace=True)

# Save merged dataset
df.to_csv("merged_weather_data.csv", index=False)

print("Merged dataset created!")
print(df.head())