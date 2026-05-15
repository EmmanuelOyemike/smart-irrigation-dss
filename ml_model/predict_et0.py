import pandas as pd
import joblib

# Load model
model = joblib.load("et0_model.pkl")

# Example future weather
future_weather = pd.DataFrame({
    "temp": [32],
    "humidity": [60],
    "wind": [2.5],
    "radiation": [20],
    "rainfall": [0]
})

# Predict ET0
prediction = model.predict(future_weather)

print("Predicted ET0:", prediction[0])