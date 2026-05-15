# Smart Irrigation Decision Support System

A smart irrigation recommendation system that combines weather data, evapotranspiration (ET₀) modelling, crop water requirement estimation, soil water balance simulation, machine learning forecasting, and a Streamlit dashboard.

---

# Features

- Historical weather data processing
- ET₀ calculation using weather variables
- Crop evapotranspiration (ETc) modelling
- Soil water balance simulation
- Irrigation decision recommendation
- Weather forecast integration using OpenWeather API
- Future irrigation schedule prediction
- Streamlit dashboard visualization
- Smart irrigation alerts

---

# Project Structure

```plaintext
irrigation-dssystem/

├── data_pipeline/
│   ├── fetch_weather.py
│   ├── fetch_rainfall.py
│   ├── merge_data.py
│   └── merged_weather_data.csv
│
├── physics_model/
│   ├── et0.py
│   ├── etc_model.py
│   ├── crop_coefficient.py
│   ├── soil_water.py
│   ├── decision.py
│   ├── run_full_model.py
│   ├── forecast_et0.py
│   ├── final_output.csv
│   └── future_irrigation_schedule.csv
│
├── ml_model/
│   ├── train_model.py
│   ├── predict_et0.py
│   ├── fetch_forecast.py
│   ├── future_irrigation.py
│   └── et0_model.pkl
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the repository

```bash
git clone <your-github-repo-link>
cd irrigation-dssystem
```

## Create virtual environment

```bash
python -m venv myenv
```

## Activate virtual environment

### Windows

```bash
myenv\Scripts\activate
```

### Mac/Linux

```bash
source myenv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the System

## Run the physics model

```bash
python physics_model/run_full_model.py
```

## Run forecast pipeline

```bash
python ml_model/fetch_forecast.py Kano
python physics_model/forecast_et0.py
python ml_model/future_irrigation.py
```

## Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

# Dashboard Features

- Historical irrigation analysis
- Future irrigation forecasting
- ET₀ visualization
- Soil moisture monitoring
- Smart irrigation alerts
- Crop selection
- Location selection

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- OpenWeather API

---

# Future Improvements

- IoT soil moisture sensor integration
- Satellite imagery integration
- Deep learning forecasting
- Mobile app deployment
- Multi-location support
- Real-time irrigation automation

---

# Author

Emmanuel Oyemike
Agricultural Engineer | Software Engineer | Precision Agriculture Enthusiast