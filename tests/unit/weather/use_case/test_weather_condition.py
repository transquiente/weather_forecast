from app.core.repository.sql import UnitOfWork
from app.location.interface import ILocationRepository
from app.weather.client import IWeatherClient, WeatherClientWeatherCurrentConditionSchema
from app.weather.domain import WeatherCondition
from app.weather.interface import IWeatherConditionRepository
from app.weather.use_case import (
    AddCurrentWeatherConditionUseCase,
    AddForecastWeatherConditionUseCase,
    GetWeatherConditionUseCase,
)
from app.weather.web import WeatherConditionDTO


def test_add_current_weather_condition_use_case_calls_repository_correctly(
    current_weather_condition: WeatherCondition,
    current_condition_weather_condition_dto: WeatherConditionDTO,
    location_repository: ILocationRepository,
    weather_condition_repository: IWeatherConditionRepository,
    weather_client: IWeatherClient,
    weather_client_weather_current_condition_schema: WeatherClientWeatherCurrentConditionSchema,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    def add_id(obj: WeatherCondition) -> WeatherCondition:
        obj.id = current_weather_condition.id
        return obj

    location = current_weather_condition.location
    location_repository.get.return_value = location
    weather_client.get_current_weather_condition_for_location.return_value = (
        weather_client_weather_current_condition_schema
    )
    weather_condition_repository.add.side_effect = lambda obj: add_id(obj)
    use_case = AddCurrentWeatherConditionUseCase(
        unit_of_work,
        location_repository,
        weather_condition_repository,
        weather_client,
    )
    # Act
    use_case.execute(current_condition_weather_condition_dto)
    # Assert
    location_repository.get.assert_called_once_with(location.id)
    weather_client.get_current_weather_condition_for_location.assert_called_once()
    weather_condition_repository.add.assert_called_once()
    weather_condition_repository.get.assert_called_once_with(current_weather_condition.id, load_refreshed=True)


def test_add_forecast_weather_condition_use_case_calls_repository_correctly(
    location_repository: ILocationRepository,
    forecast_weather_condition: WeatherCondition,
    weather_condition_repository: IWeatherConditionRepository,
    weather_client: IWeatherClient,
    weather_client_weather_current_condition_schema: WeatherClientWeatherCurrentConditionSchema,
    forecast_condition_weather_condition_dto: WeatherConditionDTO,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    def add_id(obj: WeatherCondition) -> WeatherCondition:
        obj.id = forecast_weather_condition.id
        return obj

    location = forecast_weather_condition.location
    location_repository.get.return_value = location
    weather_client.get_weather_forecast_for_location.return_value = weather_client_weather_current_condition_schema
    weather_condition_repository.add.side_effect = lambda obj: add_id(obj)
    use_case = AddForecastWeatherConditionUseCase(
        unit_of_work,
        location_repository,
        weather_condition_repository,
        weather_client,
    )
    # Act
    use_case.execute(forecast_condition_weather_condition_dto)
    # Assert
    location_repository.get.assert_called_once_with(location.id)
    weather_client.get_weather_forecast_for_location.assert_called_once()
    weather_condition_repository.add.assert_called_once()
    weather_condition_repository.get.assert_called_once_with(forecast_weather_condition.id, load_refreshed=True)


def test_get_weather_condition_use_case_calls_repository_correctly(
    current_weather_condition: WeatherCondition, weather_condition_repository: IWeatherConditionRepository
) -> None:
    # Arrange
    weather_condition_repository.get.return_value = current_weather_condition
    use_case = GetWeatherConditionUseCase(weather_condition_repository)
    # Act
    use_case.execute(current_weather_condition.id)
    # Assert
    weather_condition_repository.get.assert_called_once_with(current_weather_condition.id)
