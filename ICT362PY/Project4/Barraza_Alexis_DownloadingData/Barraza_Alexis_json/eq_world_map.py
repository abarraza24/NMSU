"""
Reads global earthquake data from a GeoJSON file and uses
Plotly to display the earthquakes on an interactive world map.
"""
from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('../data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Global Earthquakes: 30-Day Summary'
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    color=mags,
    hover_name=eq_titles,
    title=title,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
    projection='natural earth'
)

fig.show()