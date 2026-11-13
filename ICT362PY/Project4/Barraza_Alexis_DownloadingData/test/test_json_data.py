from pathlib import Path

from Barraza_Alexis_json.eq_explore_data import load_earthquake_data


def test_earthquake_data_is_extracted():
    """REQ-JSON-01: Test that earthquake features are extracted."""

    filename = Path("data/eq_data_1_day_m1.geojson")

    mags, lons, lats = load_earthquake_data(filename)

    assert len(mags) > 0
    assert len(lons) > 0
    assert len(lats) > 0


def test_earthquake_magnitudes_are_extracted():
    """REQ-JSON-02: Test that earthquake magnitudes are extracted correctly."""

    filename = Path("data/eq_data_1_day_m1.geojson")

    mags, lons, lats = load_earthquake_data(filename)

    assert mags[0] == 1.6


def test_earthquake_coordinates_are_extracted():
    """REQ-JSON-03: Test that longitude and latitude values are extracted."""

    filename = Path("data/eq_data_1_day_m1.geojson")

    mags, lons, lats = load_earthquake_data(filename)

    assert lons[0] == -150.7585
    assert lats[0] == 61.7591