import streamlit as st
import pandas as pd
import subprocess
import os

st.title("Smart Irrigation DSS")

df = pd.read_csv("../physics_model/final_output.csv")

if st.button("Refresh Dashboard"):
    st.rerun()

crop = st.selectbox(
    "Select Crop",
    ["maize", "wheat", "tomato"]
)

location = st.selectbox(
    "Select Location",
    ["Kano", "Lagos", "Abuja"]
)

if st.button("Fetch Latest Forecast"):

    subprocess.run(
        ["python", "../ml_model/fetch_forecast.py", location]
    )

    subprocess.run(
        ["python", "../physics_model/forecast_et0.py"]
    )

    subprocess.run(
        ["python", "../ml_model/future_irrigation.py"]
    )

    st.success("Forecast Updated!")

st.dataframe(
    df,
    height=800,
    use_container_width=True
)

st.subheader("System Summary")

st.metric("Average ET0", round(df["ET0"].mean(), 2))

st.metric("Minimum Soil Water", round(df["soil_water"].min(), 2))

st.metric(
    "Irrigation Events",
    (df["decision"] != "Wait").sum()
)

st.subheader("Irrigation Recommendations")

st.dataframe(
    df[["date", "ET0", "soil_water", "decision"]]
)

st.subheader("Soil Water Trend")

st.line_chart(df["soil_water"])

st.subheader("ET0 Trend")

st.line_chart(df["ET0"])

# -------------------------------
# HISTORICAL DATA
# -------------------------------

st.header("Historical Irrigation Analysis")

historical_df = pd.read_csv("../physics_model/final_output.csv")

st.subheader("Historical Dataset")

st.dataframe(
    historical_df,
    height=400,
    use_container_width=True
)

# Soil water chart
st.subheader("Historical Soil Water")

st.line_chart(historical_df["soil_water"])

etc_column = f"ETc_{crop}"

st.subheader(f"Historical {etc_column} Trend")
st.line_chart(historical_df[etc_column])

# Decision summary
st.subheader("Historical Decisions")

st.write(historical_df["decision"].value_counts())

# -------------------------------
# FUTURE FORECAST DATA
# -------------------------------

st.header("Future Irrigation Forecast")

if os.path.exists("../physics_model/future_irrigation_schedule.csv"):
    forecast_df = pd.read_csv("../physics_model/future_irrigation_schedule.csv")

irrigation_days = forecast_df[
    forecast_df["decision"] == "Irrigate"
]

if not irrigation_days.empty:

    first_day = irrigation_days.iloc[0]["date"]

    st.error(
        f"⚠ Irrigation Needed on {first_day}"
    )

    
 # -------------------------------
# SMART ALERT SYSTEM
# -------------------------------

st.subheader("Smart Irrigation Alerts")

# Latest values
latest_soil = forecast_df["soil_water"].iloc[-1]
latest_et0 = forecast_df["ET0"].max()
total_rain = forecast_df["rainfall"].sum()

# Soil moisture alert
if latest_soil < 40:
    st.error("⚠ Critical soil moisture detected. Irrigation required immediately.")

elif latest_soil < 60:
    st.warning("⚠ Soil moisture is decreasing.")

else:
    st.success("✓ Soil moisture level is healthy.")

# ET0 spike alert
if latest_et0 > 10:
    st.warning(
        f"⚠ High ET₀ forecast detected ({latest_et0:.2f}). "
        "Crop water demand may increase."
    )

# Low rainfall alert
if total_rain < 2:
    st.error(
        "⚠ Very low rainfall expected over forecast period. "
        "Irrigation planning recommended."
    )

elif total_rain < 10:
    st.warning(
        "⚠ Limited rainfall expected in coming days."
    )

else:
    st.success("✓ Sufficient rainfall expected.")

st.subheader("Forecast Irrigation Schedule")

st.dataframe(
    forecast_df,
    height=300,
    use_container_width=True
)

# Forecast ET0 chart
st.subheader("Forecast ET0")

st.line_chart(forecast_df["ET0"])

# Forecast soil water chart
st.subheader("Forecast Soil Water")

st.line_chart(forecast_df["soil_water"])

# Irrigation recommendations
st.subheader("Forecast Decisions")

st.write(forecast_df["decision"].value_counts())

#Download buttons
st.download_button(
    "Download Historical Data",
    historical_df.to_csv(index=False),
    "historical.csv",
    "text/csv"
)
st.download_button(
    "Download Forecast Data",
    forecast_df.to_csv(index=False),
    "forecast.csv",
    "text/csv"
)