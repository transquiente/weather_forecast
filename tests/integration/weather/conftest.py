from pytest_factoryboy import register

from tests.integration.core.fixtures import unit_of_work  # noqa: F401
from tests.integration.weather.fixtures import weather_condition_repository  # noqa: F401
from tests.unit.conftest import (  # noqa: F401
    LocationFactory,
    WeatherConditionFactory,
    current_weather_condition,
    location,
)

register(LocationFactory)
register(WeatherConditionFactory)
