from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from app.core.model import DATETIME_CREATED, UUID_PK, DataclassBase
from app.weather.constant import PreceptionIntensity, PreceptionType, TemperatureUnit, WindDirection, WindSpeedUnit


class WeatherCondition(DataclassBase):
    __tablename__ = "weather_forecast"

    id: Mapped[UUID_PK] = mapped_column(default=None)


class WeatherForecast(DataclassBase):
    __tablename__ = "weather_forecast"

    id: Mapped[UUID_PK] = mapped_column(default=None)
    date_time: Mapped[datetime]
    has_precipitation: Mapped[bool]
    precipitation_type: Mapped[PreceptionType | None]
    precipitation_intensity: Mapped[PreceptionIntensity | None]
    temperature_value: Mapped[Decimal]
    temperature_unit: Mapped[TemperatureUnit | None]
    real_feel_temperature_value: Mapped[Decimal]
    real_feel_temperature_unit: Mapped[TemperatureUnit | None]
    wind_speed_value: Mapped[Decimal]
    wind_speed_unit: Mapped[WindSpeedUnit | None]
    wind_direction_degrees: Mapped[Decimal]
    wind_direction_name: Mapped[WindDirection]
    relative_humidity: Mapped[int | None]
    u_v_index: Mapped[int | None]
    u_v_index_text: Mapped[str | None]
    rain_probability: Mapped[int | None]
    snow_probability: Mapped[int | None]
    ice_probability: Mapped[int | None]
    rain_value: Mapped[Decimal | None]
    rain_unit: Mapped[Decimal | None]
    snow_value: Mapped[Decimal | None]
    snow_unit: Mapped[Decimal | None]
    ice_value: Mapped[Decimal | None]
    ice_unit: Mapped[Decimal | None]
    cloud_cover: Mapped[int | None]
    solar_irradiance_value: Mapped[Decimal | None]
    solar_irradiance_unit: Mapped[Decimal | None]

    created_at: Mapped[DATETIME_CREATED] = mapped_column(init=False)
