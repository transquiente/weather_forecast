from dataclasses import dataclass

from app.core.repository.sql import ObjectNotFound
from app.location.interface import ILocationRepository
from app.location.web.schema import LocationSchema


@dataclass
class GetLocationUseCase:
    location_repository: ILocationRepository

    def execute(self, location_id) -> LocationSchema:
        location = None
        try:
            location = self.location_repository.get(location_id)
        except ObjectNotFound:
            pass
        if location is None:
            return LocationSchema(
                coordinate=None,
                country="Japan",
                state="Chiyoda City",
                city="Tokyo",
                street_address="1-1 Chiyoda",
                zip_code="100-0001",
            )
        return LocationSchema.model_validate(location)  # type: ignore
