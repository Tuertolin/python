import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

def get_coordinates(city_name):
    # First, get coordinates using a geocoding service
    # Open-Meteo provides a free geocoding API
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
            
    geo_response = requests.get(geocoding_url)
    geo_data = geo_response.json()

    if geo_response.status_code == 200:
        location_data = geo_response.json()
        if "results" in geo_data and len(geo_data["results"]) > 0:
            location = geo_data["results"][0]
            latitude = location["latitude"]
            longitude = location["longitude"]
            location_name = location["name"]
            country = location.get("country", "")
            return float(latitude), float(longitude)

def get_weather_data(lat, lon, hours):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&forecast_days=2"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to retrice weather data.")
        return None
    
st.title("Clima en tiempo real 🌤️")
st.write("Get live weather updates and forecsts.")

city_name = st.text_input("Pone la ciudad:", value="Sydney")
forecast_duration = st.slider("Entra el forcast duration en horas", min_value=12, max_value=48, value=24, step=12)
parameter_options = st.multiselect(
    "Chose weather parameter to display:",
    options=["Temp. (°C)", "Humidity (%)" ,"Wind Speed (m/s)"],
    default=["Temp. (°C)", "Humidity (%)"]
)

if st.button("Get Weather Data"):
    lat, lon = get_coordinates(city_name)
    if lat and lon:
        data = get_weather_data(lat, lon, forecast_duration)
        if data:
            times = [datetime.now() + timedelta(hours=i) for i in range(forecast_duration)]
            df = pd.DataFrame({"Time": times})

            st.subheader("Current Weather Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("🌡️ Temperature ", f"{data['hourly']['temperature_2m'][0]}°C")
            col2.metric("💧 Humidity", f"{data['hourly']['relative_humidity_2m'][0]}%")
            col3.metric("🌬️ Wind Speed", f"{data['hourly']['wind_speed_10m'][0]} m/s")
            
            if "Temperature (°C)" in parameter_options:
                df["Temperature (°C)"] = data['hourly']['temperature_2m'][:forecast_duration]
                st.subheader(f"Temperature Forecast")
                st.line_chart(df.set_index("Time")["Temperature (°C)"])

            if "Humidity (%)" in parameter_options:
                df["Humidity (%)"] = data['hourly']['relative_humidity_2m'][:forecast_duration]
                st.subheader(f"HumidityForecast")
                st.line_chart(df.set_index("Time")["Humidity (%)"])

            if "Wind Speed (m/s)" in parameter_options:
                df["Wind Speed (m/s)"] = data['hourly']['wind_speed_10m'][:forecast_duration]
                st.subheader(f"Wind SpeedForecast")
                st.line_chart(df.set_index("Time")["Wind Speed (m/s)"])

