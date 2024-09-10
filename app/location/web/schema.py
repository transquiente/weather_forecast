from pydantic_extra_types.coordinate import Coordinate, Latitude, Longitude
from typing_extensions import Self

from app.core.schema import BaseSchema
from app.location.domain import Location


class LocationSchema(BaseSchema):
    country: str | None
    state: str | None
    city: str | None
    street_address: str | None
    zip_code: str | None
    location_key: str | None
    coordinate: Coordinate | None

    @classmethod
    def model_validate(cls, obj: Location, *args, **kwargs) -> Self:
        return LocationSchema(  # type: ignore
            country=obj.country,
            state=obj.state,
            city=obj.city,
            street_address=obj.street_address,
            zip_code=obj.zip_code,
            location_key=obj.location_key,
            coordinate=Coordinate(latitude=Latitude(obj.latitude), longitude=Longitude(obj.longitude)),  # type: ignore
        )
