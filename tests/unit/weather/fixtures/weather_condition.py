from datetime import datetime, timezone
from decimal import Decimal
from random import randint
from uuid import uuid4

import factory
import pytest
from pytest_factoryboy import register
from pytest_mock import MockerFixture

from app.weather.constant import (
    PrecipitationIntensity,
    PrecipitationType,
    SolarIrradianceUnit,
    TemperatureUnit,
    WeatherDataType,
    WindDirection,
    WindSpeedUnit,
)
from app.weather.domain import WeatherCondition
from app.weather.interface import IWeatherConditionRepository
from app.weather.web import WeatherConditionDTO
from tests.unit.location.fixtures import LocationFactory

register(LocationFactory)


@pytest.fixture
def weather_condition_repository(mocker: MockerFixture) -> IWeatherConditionRepository:
    return mocker.Mock(spec=IWeatherConditionRepository)


class WeatherConditionFactory(factory.Factory):
    class Meta:
        model = WeatherCondition

    id = factory.LazyFunction(uuid4)
    data_type = WeatherDataType.CURRENT_CONDITION
    date_time = factory.LazyFunction(lambda: datetime.now(tz=timezone.utc).replace(tzinfo=None))
    weather_text = factory.Sequence(lambda wtxt: f"weather text {wtxt}")
    has_precipitation = factory.LazyFunction(lambda: randint(0, 1) == 1)
    precipitation_type = PrecipitationType.RAIN
    precipitation_intensity = PrecipitationIntensity.LIGHT
    temperature_value = Decimal("25")
    temperature_unit = TemperatureUnit.CELSIUS
    real_feel_temperature_value = Decimal("24")
    real_feel_temperature_unit = TemperatureUnit.CELSIUS
    wind_speed_value = Decimal("0")
    wind_speed_unit = WindSpeedUnit.METERS_PER_SECOND
    wind_direction_degrees = factory.LazyFunction(lambda: randint(0, 7))
    wind_direction_name = WindDirection.EAST
    relative_humidity = factory.LazyFunction(lambda: randint(0, 10))
    u_v_index = factory.LazyFunction(lambda: randint(0, 10))
    u_v_index_text = factory.Sequence(lambda txt: f"u_v_index_text {txt}")
    rain_probability = factory.LazyFunction(lambda: randint(0, 10))
    snow_probability = factory.LazyFunction(lambda: randint(0, 10))
    ice_probability = factory.LazyFunction(lambda: randint(0, 10))
    rain_value = None
    rain_unit = None
    snow_value = None
    snow_unit = None
    ice_value = None
    ice_unit = None
    cloud_cover = factory.LazyFunction(lambda: randint(0, 100))
    solar_irradiance_value = Decimal("3")
    solar_irradiance_unit = SolarIrradianceUnit.WATT_PER_SQUARE_METRE
    location = factory.SubFactory(LocationFactory)
    location_id = factory.LazyAttribute(lambda obj: obj.location.id)


@pytest.fixture
def current_weather_condition(weather_condition_factory: type[WeatherConditionFactory]) -> WeatherCondition:
    weather_condition = weather_condition_factory()
    return weather_condition


@pytest.fixture
def forecast_weather_condition(weather_condition_factory: type[WeatherConditionFactory]) -> WeatherCondition:
    weather_condition = weather_condition_factory()
    return weather_condition


@pytest.fixture
def current_condition_weather_condition_dto(current_weather_condition: WeatherCondition) -> WeatherConditionDTO:
    return WeatherConditionDTO(
        location_id=current_weather_condition.location_id,
        data_type=WeatherDataType.CURRENT_CONDITION,
    )


@pytest.fixture
def forecast_condition_weather_condition_dto(forecast_weather_condition: WeatherCondition) -> WeatherConditionDTO:
    return WeatherConditionDTO(
        location_id=forecast_weather_condition.location_id,
        data_type=WeatherDataType.FORECAST_CONDITION,
    )
