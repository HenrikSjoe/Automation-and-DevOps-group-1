import requests
from weather_api_call import get_weather


def test_api_works():
    """Kollar om väder-API:et går att nå"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 59.33,
        "longitude": 18.06,
        "hourly": "temperature_2m",
        "timezone": "Europe/Stockholm"
    }
    r = requests.get(url, params=params)
    assert r.status_code == 200


def test_get_weather_not_empty():
    """Kollar att funktionen get_weather faktiskt returnerar något"""
    result = get_weather()
    assert result is not None


def test_get_weather_has_columns():
    """Kollar att resultatet har rätt kolumner"""
    df = get_weather()
    assert "time" in df.columns
    assert "temperature" in df.columns


def test_dataframe_not_empty():
    """Testar att DataFrame inte är tom"""
    df = get_weather()
    assert len(df) > 0


def test_temperature_not_null():
    """Testar att temperatur inte är tom"""
    df = get_weather()
    assert df["temperature"].isnull().sum() == 0


def test_time_not_null():
    """Testar att tid inte är tom"""
    df = get_weather()
    assert df["time"].isnull().sum() == 0
