from pydantic import field_validator
from pydantic_extra_types.coordinate import Coordinate, Latitude, Longitude

from app.core.schema import BaseSchema


class LocationSchema(BaseSchema):
    coordinate: Coordinate | None
    country: str | None
    state: str | None
    city: str | None
    street_address: str | None
    zip_code: str | None

    @field_validator("coordinate")
    @classmethod
    def validate_coordinate(cls, coordinate: Coordinate | None) -> Coordinate:
        if not coordinate:
            return Coordinate(latitude=Latitude(35.68518230181968), longitude=Longitude(139.75279840684516))
