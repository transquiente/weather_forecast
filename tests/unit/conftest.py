from pytest_factoryboy import register

from .core.conftest import unit_of_work  # noqa: F401
from .location.conftest import (  # noqa: F401
    LocationFactory,
    create_location_dto,
    location,
    location_client,
    location_client_location_schema,
    location_repository,
    update_location_dto,
)
from .weather.conftest import (  # noqa: F401
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
