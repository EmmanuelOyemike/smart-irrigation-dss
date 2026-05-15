import pandas as pd

# Load ET0 forecast
df = pd.read_csv("forecast_et0_output.csv")

# Crop coefficient for maize
Kc = 1.2

# Compute ETc
df["ETc_maize"] = df["ET0"] * Kc

# Initial soil water
soil_water = 100

soil_list = []
decision_list = []

for _, row in df.iterrows():

    rainfall = row["rainfall"]
    etc = row["ETc_maize"]

    # Soil water balance
    soil_water = soil_water + rainfall - etc

    # Keep within limits
    soil_water = max(0, min(100, soil_water))

    soil_list.append(soil_water)

    # Irrigation decision
    if soil_water < 40:
        decision = "Irrigate"
    else:
        decision = "Wait"

    decision_list.append(decision)

# Save outputs
df["soil_water"] = soil_list
df["decision"] = decision_list

df.to_csv("future_irrigation_schedule.csv", index=False)

print(df[["date", "ET0", "soil_water", "decision"]].head())

print("Future irrigation schedule generated!")