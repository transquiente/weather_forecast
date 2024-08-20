from dataclasses import dataclass
from uuid import UUID

from app.core.exception import ValidationError
from app.core.repository.sql import UnitOfWork
from app.location.interface import ILocationRepository
from app.weather.client import IWeatherClient
from app.weather.domain import WeatherCondition
from app.weather.interface import IWeatherConditionRepository
from app.weather.web import WeatherConditionDTO


@dataclass
class AddCurrentWeatherConditionUseCase:
    uow: UnitOfWork
    location_repository: ILocationRepository
    weather_condition_repository: IWeatherConditionRepository
    weather_client: IWeatherClient

    def execute(self, weather_condition_dto: WeatherConditionDTO) -> WeatherCondition:
        location = self.location_repository.get(weather_condition_dto.location_id)
        if location.location_key is None:
            raise ValidationError(
                f"Location {location.id} has no location key, so it cannot be used for weather condition check."
            )
        current_weather_from_weather_client = self.weather_client.get_current_weather_condition_for_location(
            location_key=location.location_key,
            details=True,
        )
        with self.uow:
            weather = weather_condition_dto.from_dto(current_weather_from_weather_client)
            self.weather_condition_repository.add(weather)
        weather = self.weather_condition_repository.get(weather.id, load_refreshed=True)
        return weather


@dataclass
class AddForecastWeatherConditionUseCase:
    uow: UnitOfWork
    location_repository: ILocationRepository
    weather_condition_repository: IWeatherConditionRepository
    weather_client: IWeatherClient

    def execute(self, weather_condition_dto: WeatherConditionDTO) -> WeatherCondition:
        location = self.location_repository.get(weather_condition_dto.location_id)
        if location.location_key is None:
            raise ValidationError(
                f"Location {location.id} has no location key, so it cannot be used for weather forecast."
            )
        weather_forecast_from_weather_client = self.weather_client.get_weather_forecast_for_location(
            location_key=location.location_key,
            details=True,
            metric=True,
        )
        with self.uow:
            weather = weather_condition_dto.from_dto(weather_forecast_from_weather_client)
            self.weather_condition_repository.add(weather)
        weather = self.weather_condition_repository.get(weather.id, load_refreshed=True)
        return weather


@dataclass
class GetWeatherConditionUseCase:
    weather_condition_repository: IWeatherConditionRepository

    def execute(self, weather_condition_id: UUID) -> WeatherCondition:
        return self.weather_condition_repository.get(weather_condition_id)
