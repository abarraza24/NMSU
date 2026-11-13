"""
Reads Death Valley weather data from a CSV file and plots
the high and low temperatures while handling missing data.
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt


def load_weather_data(filename):
    """Read dates, high temperatures, and low temperatures from a CSV file."""

    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')

            try:
                high = int(row[3])
                low = int(row[4])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows


if __name__ == "__main__":
    filename = "data/death_valley_2021_simple.csv"

    dates, highs, lows = load_weather_data(filename)

    # Plot the high and low temp.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
    ax.set_title(title, fontsize=20)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()
