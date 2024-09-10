from pytest_factoryboy import register

from tests.unit.core.conftest import unit_of_work  # noqa: F401
from tests.unit.location.fixtures import (  # noqa: F401
    LocationFactory,
    location_repository,
)
from tests.unit.weather.fixtures import (  # noqa: F401
    WeatherConditionFactory,
    current_condition_weather_condition_dto,
    current_weather_condition,
    forecast_condition_weather_condition_dto,
    forecast_weather_condition,
    weather_client,
    weather_client_weather_current_condition_schema,
    weather_client_weather_forecast_condition_schema,
    weather_condition_repository,
)

register(LocationFactory)
register(WeatherConditionFactory)
