from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.model import DATETIME_CREATED, UUID_PK, DataclassBase
from app.location.domain import Location
from app.weather.constant import (
    PrecipitationIntensity,
    PrecipitationType,
    PrecipitationUnit,
    SolarIrradianceUnit,
    TemperatureUnit,
    WeatherDataType,
    WindDirection,
    WindSpeedUnit,
)


class WeatherCondition(DataclassBase):
    __tablename__ = "weather_condition"

    id: Mapped[UUID_PK] = mapped_column(default=None)
    location_id: Mapped[UUID] = mapped_column(
        ForeignKey("location.id", ondelete="CASCADE", name="weather_location_id_fkey"),
        index=True,
    )

    data_type: Mapped[WeatherDataType]
    date_time: Mapped[datetime] = mapped_column(index=True)
    weather_text: Mapped[str | None]
    has_precipitation: Mapped[bool]
    precipitation_type: Mapped[PrecipitationType | None]
    precipitation_intensity: Mapped[PrecipitationIntensity | None]
    temperature_value: Mapped[Decimal]
    temperature_unit: Mapped[TemperatureUnit]
    real_feel_temperature_value: Mapped[Decimal]
    real_feel_temperature_unit: Mapped[TemperatureUnit]
    wind_speed_value: Mapped[Decimal]
    wind_speed_unit: Mapped[WindSpeedUnit]
    wind_direction_degrees: Mapped[int]
    wind_direction_name: Mapped[WindDirection]
    relative_humidity: Mapped[int | None]
    u_v_index: Mapped[int | None]
    u_v_index_text: Mapped[str | None]
    rain_probability: Mapped[int | None]
    snow_probability: Mapped[int | None]
    ice_probability: Mapped[int | None]
    rain_value: Mapped[Decimal | None]
    rain_unit: Mapped[PrecipitationUnit | None]
    snow_value: Mapped[Decimal | None]
    snow_unit: Mapped[PrecipitationUnit | None]
    ice_value: Mapped[Decimal | None]
    ice_unit: Mapped[PrecipitationUnit | None]
    cloud_cover: Mapped[int | None]
    solar_irradiance_value: Mapped[Decimal | None]
    solar_irradiance_unit: Mapped[SolarIrradianceUnit | None]

    location: Mapped[Location] = relationship(
        foreign_keys=[location_id],
        back_populates="weather_information",
        default=None,
        compare=False,
        lazy="joined",  # because many-to-one side
    )

    created_at: Mapped[DATETIME_CREATED] = mapped_column(init=False)
