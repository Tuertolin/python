
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

# ===== WEATHER SECTION =====
with col1:
    st.header("Weather Updates")
    
    # City input
    city = st.text_input("Enter city name:", "London")
    
    if st.button("Get Weather"):
        # Using OpenWeatherMap API (you'll need to sign up for a free API key)
        # For demo purposes, showing the structure
        st.info("Note: You'll need to sign up for a free API key at openweathermap.org")
        
        # Example API call structure:
        # api_key = "YOUR_API_KEY"
        # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        # response = requests.get(url)
        # data = response.json()
        
        # Demo data display
        st.subheader(f"Weather in {city}")
        st.metric("Temperature", "22°C", "2°C")
        st.metric("Humidity", "65%")
        st.metric("Wind Speed", "15 km/h")

# ===== STOCK SECTION =====
with col2:
    st.header("Stock Price Updates")
    
    # Stock ticker input
    ticker = st.text_input("Enter stock ticker:", "AAPL")
    
    # Date range selector
    days = st.slider("Select number of days:", 7, 90, 30)
    
    if st.button("Get Stock Data"):
        try:
            # Fetch stock data using yfinance
            stock = yf.Ticker(ticker)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            
            # Get historical data
            hist = stock.history(start=start_date, end=end_date)
            
            if not hist.empty:
                # Display current price
                current_price = hist['Close'].iloc[-1]
                prev_price = hist['Close'].iloc[-2]
                change = current_price - prev_price
                
                st.subheader(f"{ticker} Stock Information")
                st.metric("Current Price", f"${current_price:.2f}", f"${change:.2f}")
                
                # Display line chart
                st.line_chart(hist['Close'])
                
                # Display data table
                st.subheader("Recent Data")
                st.dataframe(hist.tail(10))
            else:
                st.error("No data found for this ticker")
                
        except Exception as e:
            st.error(f"Error fetching stock data: {str(e)}")

# ===== REFRESH SECTION =====
st.divider()
if st.button("🔄 Refresh All Data"):
    st.rerun()

# Footer
st.caption("Dashboard updates in real-time when you click the buttons above")

