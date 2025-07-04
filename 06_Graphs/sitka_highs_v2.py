import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = './sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, low and high temp for this file
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = ((int(row[5]) -32) / 1.8)
        low = ((int(row[6]) -32) / 1.8)
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    print(highs)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Plot the high and low temp
plt.style.use('seaborn')
fig, ax = plt.subplots() 

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temp - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temp (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# What is next? --> Plotting a Longer Timeframe
