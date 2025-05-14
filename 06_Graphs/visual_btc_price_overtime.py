import csv
from datetime import datetime, timezone
import matplotlib.pyplot as plt
import time


date_to_compare = datetime(2024, 11, 17)

filename = './bitcoin_UpdatedMay_v22025.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, low and high temp for this file
    dates, highs = [], []
    for row in reader:
        epoch_ms = int(row[0])
        current_date = datetime.fromtimestamp(epoch_ms / 1000)

        if current_date > date_to_compare:
            print(current_date)
            dates.append(current_date)
            high = int(float(row[5]))
            highs.append(high)
        

# Plot the high and low temp
plt.style.use('seaborn')
fig, ax = plt.subplots() 
ax.plot(dates, highs, c='red')

# Format plot
plt.title("Daily high over time", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("USD $", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

