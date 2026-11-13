from pathlib import Path
from datetime import datetime

from Barraza_Alexis_csv.death_valley_high import load_weather_data


def test_csv_data_can_be_read():
    """REQ-CSV-01: Test that weather data can be read from the CSV file."""

    filename = Path("data/death_valley_2021_simple.csv")

    dates, highs, lows = load_weather_data(filename)

    assert len(dates) > 0
    assert len(highs) > 0
    assert len(lows) > 0


def test_dates_are_datetime_objects():
    """REQ-CSV-02: Test that CSV date strings are converted to datetime objects."""

    filename = Path("data/death_valley_2021_simple.csv")

    dates, highs, lows = load_weather_data(filename)

    assert isinstance(dates[0], datetime)


def test_temperature_values_are_integers():
    """REQ-CSV-03: Test that high and low temperatures are converted to integers."""

    filename = Path("data/death_valley_2021_simple.csv")

    dates, highs, lows = load_weather_data(filename)

    assert isinstance(highs[0], int)
    assert isinstance(lows[0], int)