import sys
from pathlib import Path

import chromedriver_binary  # noqa: F401

sys.path.append(str(Path(__file__).resolve().parents[1]))

import app


def test_header_present(dash_duo):
    dash_duo.start_server(app.app)
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Visualiser")
    assert dash_duo.find_element("h1").is_displayed()


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app.app)
    dash_duo.wait_for_element_by_id("sales-chart")
    svg = dash_duo.wait_for_element("#sales-chart .main-svg")
    assert svg.is_displayed()


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app.app)
    picker = dash_duo.wait_for_element_by_id("region-radio")
    assert picker.is_displayed()
