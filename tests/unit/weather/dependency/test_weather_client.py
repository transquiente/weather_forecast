from app.weather.client import IWeatherClient, get_weather_client_settings
from app.weather.dependency import get_weather_client


def test_get_weather_client_returns_weather_client():
    assert isinstance(get_weather_client(settings=get_weather_client_settings()), IWeatherClient)
