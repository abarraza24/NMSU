"""
Reads earthquake data from a GeoJSON file and extracts
the magnitude, longitude, and latitude values.
"""

from pathlib import Path
import json


def load_earthquake_data(filename):
    """Read earthquake magnitude and coordinate data from a GeoJSON file."""

    path = Path(filename)
    contents = path.read_text(encoding='utf-8')
    all_eq_data = json.loads(contents)

    all_eq_dicts = all_eq_data['features']

    mags, lons, lats = [], [], []

    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]

        mags.append(mag)
        lons.append(lon)
        lats.append(lat)

    return mags, lons, lats


if __name__ == "__main__":
    filename = "data/eq_data_1_day_m1.geojson"

    mags, lons, lats = load_earthquake_data(filename)

    print(mags[:10])
    print(lons[:5])
    print(lats[:5])