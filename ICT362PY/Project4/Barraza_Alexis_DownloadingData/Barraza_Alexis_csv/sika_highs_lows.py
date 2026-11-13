"""
Reads weather data from a CSV file and plots the daily
high and low temperatures for Sitka using Matplotlib.
"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = '../data/sitka_weather_07-2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Get dates, high and low temperatures from the file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
        
# Plot the high and low tempratures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

# Added for visual effects
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title("Daily high and low temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()


plt.show()