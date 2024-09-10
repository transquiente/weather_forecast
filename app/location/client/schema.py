from decimal import Decimal

from pydantic import AliasGenerator, ConfigDict, Field, model_validator
from pydantic.alias_generators import to_pascal, to_snake

from app.core.schema import BaseSchema


class LocationClientBaseSchema(BaseSchema):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_pascal,
            serialization_alias=to_snake,
        )
    )


class LocationClientCountrySchema(LocationClientBaseSchema):
    id: str = Field(alias="ID")
    english_name: str


class AdministrativeAreaSchema(LocationClientBaseSchema):
    id: str = Field(alias="ID")
    english_name: str
    english_type: str


class LocationClientGeoPositionSchema(LocationClientBaseSchema):
    latitude: Decimal
    longitude: Decimal
    elevation: Decimal | None

    @model_validator(mode="before")
    @classmethod
    def validate_elevation(cls, data: dict) -> dict:
        if data.get("Elevation") is None:
            return data
        data["Elevation"] = data.get("Elevation", {}).get("Metric", {}).get("Value", {})
        return data


class LocationClientLocationSchema(LocationClientBaseSchema):
    key: str
    english_name: str
    primary_postal_code: str | None
    country: LocationClientCountrySchema | None
    administrative_area: AdministrativeAreaSchema | None
    geo_position: LocationClientGeoPositionSchema | None
