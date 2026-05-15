import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
import joblib

# Load dataset
df = pd.read_csv("../data_pipeline/final_output.csv")

# Features
X = df[["temp", "humidity", "wind", "radiation", "rainfall"]]

# Target
y = df["ET0"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4
)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)

print("MAE:", mae)

# Save model
joblib.dump(model, "et0_model.pkl")

print("Model saved!")

plt.figure(figsize=(10,5))

plt.plot(y_test.values, label="Actual ET0")
plt.plot(predictions, label="Predicted ET0")

plt.legend()
plt.title("ET0 Forecasting")

plt.xlabel("Test Samples")
plt.ylabel("ET0")

plt.show()