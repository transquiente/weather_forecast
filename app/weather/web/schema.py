from datetime import datetime
from decimal import Decimal
from uuid import UUID

from app.core.schema import BaseSchema
from app.weather.constant import (
    PrecipitationIntensity,
    PrecipitationType,
    TemperatureUnit,
    WeatherDataType,
    WindDirection,
    WindSpeedUnit,
)


class LocationShortSchema(BaseSchema):
    country: str | None
    state: str | None
    city: str | None
    latitude: Decimal | None
    longitude: Decimal | None


class WeatherSchema(BaseSchema):
    id: UUID
    location: LocationShortSchema
    data_type: WeatherDataType
    date_time: datetime
    has_precipitation: bool
    precipitation_type: PrecipitationType | None
    precipitation_intensity: PrecipitationIntensity | None
    temperature_value: Decimal
    temperature_unit: TemperatureUnit
    real_feel_temperature_value: Decimal
    real_feel_temperature_unit: TemperatureUnit
    wind_speed_value: Decimal
    wind_speed_unit: WindSpeedUnit
    wind_direction_degrees: int
    wind_direction_name: WindDirection
    relative_humidity: int | None
    u_v_index: int | None
    u_v_index_text: str | None
    rain_probability: int | None
    snow_probability: int | None
    ice_probability: int | None
    rain_value: Decimal | None
    rain_unit: str | None
    snow_value: Decimal | None
    snow_unit: str | None
    ice_value: Decimal | None
    ice_unit: str | None
    cloud_cover: int | None
    solar_irradiance_value: Decimal | None
    solar_irradiance_unit: str | None

    class Config:
        from_attributes = True
