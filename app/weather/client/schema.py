from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

from pydantic import AliasGenerator, ConfigDict, Field, model_validator
from pydantic.alias_generators import to_pascal, to_snake

from app.core.schema import BaseSchema
from app.weather.constant import PrecipitationIntensity, PrecipitationType


class WeatherClientBaseSchema(BaseSchema):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_pascal,
            serialization_alias=to_snake,
        )
    )


class UnitSchema(WeatherClientBaseSchema):
    value: Decimal
    unit: str
    unit_type: int


class EnclosureUnitSchema(WeatherClientBaseSchema):
    metric: UnitSchema
    imperial: UnitSchema


class DirectionSchema(WeatherClientBaseSchema):
    degrees: int
    english: str


class PrecipitationSummarySchema(WeatherClientBaseSchema):
    precipitation: EnclosureUnitSchema


class WindSchema(WeatherClientBaseSchema):
    direction: DirectionSchema
    speed: EnclosureUnitSchema


class WindForecastSchema(WeatherClientBaseSchema):
    direction: DirectionSchema
    speed: UnitSchema


class WeatherClientWeatherCurrentConditionSchema(WeatherClientBaseSchema):
    local_observation_date_time: datetime
    weather_text: str | None
    has_precipitation: bool
    precipitation_type: PrecipitationType | None
    precipitation_intensity: PrecipitationIntensity | None = None
    precipitation_summary: PrecipitationSummarySchema
    precip_1hr: EnclosureUnitSchema = Field(alias="Precip1hr")
    pressure: EnclosureUnitSchema
    cloud_cover: int
    visibility: EnclosureUnitSchema
    u_v_index: int | None
    u_v_index_text: str | None
    wind: WindSchema
    dew_point: EnclosureUnitSchema
    relative_humidity: int | None
    temperature: EnclosureUnitSchema
    real_feel_temperature: EnclosureUnitSchema

    @model_validator(mode="before")
    @classmethod
    def parse_local_observation_date_time(cls, data: Any) -> Any:
        if isinstance(data, dict):
            local_observation_date_time = data.get("LocalObservationDateTime")
            if local_observation_date_time is not None:
                data["LocalObservationDateTime"] = datetime.fromisoformat(local_observation_date_time).astimezone(
                    timezone.utc
                )
        return data


class WeatherClientWeatherForecastConditionSchema(WeatherClientBaseSchema):
    date_time: datetime
    icon_phrase: str | None
    has_precipitation: bool
    temperature: UnitSchema
    real_feel_temperature: UnitSchema
    dew_point: UnitSchema
    wind: WindForecastSchema
    relative_humidity: int | None
    visibility: UnitSchema
    u_v_index: int | None
    u_v_index_text: str | None
    precipitation_probability: int | None
    thunderstorm_probability: int | None
    rain_probability: int | None
    snow_probability: int | None
    ice_probability: int | None
    rain: UnitSchema
    snow: UnitSchema
    ice: UnitSchema
    cloud_cover: int
    solar_irradiance: UnitSchema

    @model_validator(mode="before")
    @classmethod
    def parse_local_observation_date_time(cls, data: Any) -> Any:
        if isinstance(data, dict):
            date_time = data.get("DateTime")
            if date_time is not None:
                data["DateTime"] = datetime.fromisoformat(date_time).astimezone(timezone.utc)
        return data
