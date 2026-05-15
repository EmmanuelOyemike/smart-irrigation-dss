import pandas as pd
import matplotlib.pyplot as plt
from et0 import compute_et0
from etC_model import compute_etc
from soil_water import compute_soil_water
from decision import irrigation_decision

# Load merged dataset
df = pd.read_csv("../data_pipeline/merged_weather_data.csv")

# Step 1: ET0
df = compute_et0(df)

# Step 2: ETc
df = compute_etc(df)

# Step 3: Soil water
df = compute_soil_water(df, crop="maize")

# Step 4: Decision
df = irrigation_decision(df)

# Save final output
df.to_csv("final_output.csv", index=False)

# Show first rows
print(df.head())

# Decision counts
print(df["decision"].value_counts())

# Plot soil water
plt.figure(figsize=(12,5))
plt.plot(df["soil_water"])

# Irrigation threshold
plt.axhline(y=40, linestyle="--")

plt.title("Soil Water Balance")
plt.xlabel("Days")
plt.ylabel("Soil Water")

plt.show()

print(df.head())
print(df[["ET0", "ETc_maize", "soil_water"]].describe())