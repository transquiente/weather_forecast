from fastapi import Depends

from app.weather.client import IWeatherClient, WeatherClient, WeatherClientSettings, get_weather_client_settings


def get_weather_client(
    settings: WeatherClientSettings = Depends(get_weather_client_settings),
) -> IWeatherClient:
    return WeatherClient(settings)
