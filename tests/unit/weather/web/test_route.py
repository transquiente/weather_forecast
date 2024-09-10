import pytest
from pytest_mock import MockFixture

from app.core.repository import UnitOfWork
from app.location.interface import ILocationRepository
from app.weather.client import IWeatherClient
from app.weather.domain import WeatherCondition
from app.weather.interface import IWeatherConditionRepository
from app.weather.web import WeatherConditionDTO
from app.weather.web.route import add_weather_condition, get_weather_condition_for_location


def test_add_current_weather_condition_should_create_and_return_weather_condition(
    execute_add_current_weather_condition_use_case_mock: MockFixture,
    current_weather_condition: WeatherCondition,
    current_condition_weather_condition_dto: WeatherConditionDTO,
    weather_condition_repository: IWeatherConditionRepository,
    location_repository: ILocationRepository,
    weather_client: IWeatherClient,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    execute_add_current_weather_condition_use_case_mock.return_value = current_weather_condition
    # Act
    add_current_weather_condition_response = add_weather_condition(
        current_condition_weather_condition_dto,
        unit_of_work,
        weather_condition_repository,
        location_repository,
        weather_client,
    )
    # Assert
    assert add_current_weather_condition_response is not None


def test_add_forecast_weather_condition_should_create_and_return_weather_condition(
    execute_add_forecast_weather_condition_use_case_mock: MockFixture,
    forecast_weather_condition: WeatherCondition,
    forecast_condition_weather_condition_dto: WeatherConditionDTO,
    weather_condition_repository: IWeatherConditionRepository,
    location_repository: ILocationRepository,
    weather_client: IWeatherClient,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    execute_add_forecast_weather_condition_use_case_mock.return_value = forecast_weather_condition
    # Act
    add_forecast_weather_condition_response = add_weather_condition(
        forecast_condition_weather_condition_dto,
        unit_of_work,
        weather_condition_repository,
        location_repository,
        weather_client,
    )
    # Assert
    assert add_forecast_weather_condition_response is not None


def test_get_location_should_return_location(
    execute_get_weather_condition_use_case_mock: MockFixture,
    current_weather_condition: WeatherCondition,
    weather_condition_repository: IWeatherConditionRepository,
) -> None:
    # Arrange
    execute_get_weather_condition_use_case_mock.return_value = current_weather_condition
    # Act
    get_weather_condition_response = get_weather_condition_for_location(
        current_weather_condition.id, weather_condition_repository
    )
    # Assert
    assert get_weather_condition_response is not None


@pytest.fixture
def execute_add_current_weather_condition_use_case_mock(
    mocker: MockFixture,
) -> MockFixture:
    return mocker.patch("app.weather.web.route.AddCurrentWeatherConditionUseCase.execute")


@pytest.fixture
def execute_add_forecast_weather_condition_use_case_mock(
    mocker: MockFixture,
) -> MockFixture:
    return mocker.patch("app.weather.web.route.AddForecastWeatherConditionUseCase.execute")


@pytest.fixture
def execute_get_weather_condition_use_case_mock(
    mocker: MockFixture,
) -> MockFixture:
    return mocker.patch("app.weather.web.route.GetWeatherConditionUseCase.execute")
