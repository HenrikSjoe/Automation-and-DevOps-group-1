import pandas as pd
from unittest.mock import patch
from weather_api_call import get_weather


@patch('weather_api_call.requests.get')
def test_get_weather_mock(mock_get):
    mock_get.return_value.json.return_value = {
        "hourly": {
            "time": ["2024-11-10T10:00", "2024-11-10T11:00"],
            "temperature_2m": [15.0, "16.0"]
        }
    }

    result = get_weather()
    assert isinstance(result, pd.DataFrame)


@patch('weather_api_call.requests.get')
def test_columns(mock_get):
    mock_get.return_value.json.return_value = {
        "hourly": {
            "time": ["2024-11-10T10:00"],
            "temperature_2m": [15.0]
        }
    }

    result = get_weather()
    assert "time" in result.columns
    assert "temperature" in result.columns


@patch('weather_api_call.requests.get')
def test_temperature_type(mock_get):
    mock_get.return_value.json.return_value = {
        "hourly": {
            "time": ["2024-11-10T10:00"],
            "temperature_2m": [15.0]
        }
    }

    result = get_weather()
    assert pd.api.types.is_numeric_dtype(result["temperature"])
