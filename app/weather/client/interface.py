from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.weather.client.schema import (
    WeatherClientWeatherCurrentConditionSchema,
    WeatherClientWeatherForecastConditionSchema,
)


@dataclass
class IWeatherClient(ABC):
    @abstractmethod
    def get_current_weather_condition_for_location(
        self,
        location_key: str,
        details: bool = False,
    ) -> WeatherClientWeatherCurrentConditionSchema:
        raise NotImplementedError

    @abstractmethod
    def get_weather_forecast_for_location(
        self,
        location_key: str,
        details: bool = False,
        metric: bool = False,
    ) -> WeatherClientWeatherForecastConditionSchema:
        raise NotImplementedError
