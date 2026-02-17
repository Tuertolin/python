import streamlit as st
import pandas as pd
import requests
import yfinance as yf
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Weather & Stock Dashboard", layout="wide")

# Title
st.title("🌤️ Weather & 📈 Stock Price Dashboard")

# Create two columns for layout
col1, col2 = st.columns(2)

# ===== WEATHER SECTION WITH OPEN-METEO =====
with col1:
    st.header("Weather Updates (Open-Meteo)")
    
    # City input with Australian cities as examples
    city = st.text_input("Enter city name:", "Sydney")
    
    if st.button("Get Weather"):
        try:
            # First, get coordinates using a geocoding service
            # Open-Meteo provides a free geocoding API
            geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
            geo_response = requests.get(geocoding_url)
            geo_data = geo_response.json()
            
            if "results" in geo_data and len(geo_data["results"]) > 0:
                location = geo_data["results"][0]
                latitude = location["latitude"]
                longitude = location["longitude"]
                location_name = location["name"]
                country = location.get("country", "")
                
                st.subheader(f"Weather in {location_name}, {country}")
                
                # Get weather data from Open-Meteo
                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m&timezone=auto"
                weather_response = requests.get(weather_url)
                weather_data = weather_response.json()
                
                if "current" in weather_data:
                    current = weather_data["current"]
                    
                    # Temperature
                    temp = current["temperature_2m"]
                    feels_like = current["apparent_temperature"]
                    st.metric("Temperature", f"{temp}°C", f"Feels like {feels_like}°C")
                    
                    # Humidity
                    humidity = current["relative_humidity_2m"]
                    st.metric("Humidity", f"{humidity}%")
                    
                    # Wind Speed
                    wind_speed = current["wind_speed_10m"]
                    st.metric("Wind Speed", f"{wind_speed} km/h")
                    
                    # Precipitation
                    precipitation = current["precipitation"]
                    st.metric("Precipitation", f"{precipitation} mm")
                    
                    # Weather code interpretation
                    weather_code = current["weather_code"]
                    weather_descriptions = {
                        0: "Clear sky ☀️",
                        1: "Mainly clear 🌤️",
                        2: "Partly cloudy ⛅",
                        3: "Overcast ☁️",
                        45: "Foggy 🌫️",
                        48: "Depositing rime fog 🌫️",
                        51: "Light drizzle 🌦️",
                        53: "Moderate drizzle 🌦️",
                        55: "Dense drizzle 🌦️",
                        61: "Slight rain 🌧️",
                        63: "Moderate rain 🌧️",
                        65: "Heavy rain 🌧️",
                        71: "Slight snow ❄️",
                        73: "Moderate snow ❄️",
                        75: "Heavy snow ❄️",
                        95: "Thunderstorm ⛈️"
                    }
                    weather_desc = weather_descriptions.get(weather_code, "Unknown conditions")
                    st.info(f"Conditions: {weather_desc}")
                    
                    # Display coordinates
                    st.caption(f"Coordinates: {latitude}°, {longitude}°")
                else:
                    st.error("Unable to retrieve weather data")
            else:
                st.error(f"City '{city}' not found. Please try another city name.")
                
        except Exception as e:
            st.error(f"Error fetching weather data: {str(e)}")

# ===== STOCK SECTION =====
with col2:
    st.header("Stock Price Updates")
    
    # Stock ticker input with Australian examples
    ticker = st.text_input("Enter stock ticker:", "CBA.AX", 
                          help="For Australian stocks, add .AX (e.g., CBA.AX, BHP.AX)")
    days = st.slider("Select number of days:", 7, 90, 30)
    
    if st.button("Get Stock Data"):
        try:
            stock = yf.Ticker(ticker)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            
            # Get historical data
            hist = stock.history(start=start_date, end=end_date)
            
            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                prev_price = hist['Close'].iloc[-2]
                change = current_price - prev_price
                change_pct = (change / prev_price) * 100
                
                st.subheader(f"{ticker} Stock Information")
                st.metric("Current Price", f"${current_price:.2f}", 
                         f"${change:.2f} ({change_pct:+.2f}%)")
                
                # Display line chart
                st.line_chart(hist['Close'])
                
                # Display data table
                st.subheader("Recent Data")
                display_hist = hist[['Open', 'High', 'Low', 'Close', 'Volume']].tail(10)
                st.dataframe(display_hist.style.format({
                    'Open': '${:.2f}',
                    'High': '${:.2f}',
                    'Low': '${:.2f}',
                    'Close': '${:.2f}',
                    'Volume': '{:,.0f}'
                }))
            else:
                st.error("No data found for this ticker. Make sure to use the correct format (e.g., CBA.AX for Australian stocks)")
                
        except Exception as e:
            st.error(f"Error fetching stock data: {str(e)}")

# ===== REFRESH SECTION =====
st.divider()
if st.button("🔄 Refresh All Data"):
    st.rerun()

st.caption("Dashboard updates in real-time when you click the buttons above")
st.caption("Weather data provided by Open-Meteo API (free, no API key required)")

