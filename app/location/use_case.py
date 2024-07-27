from dataclasses import dataclass

from app.location.web.schema import LocationSchema


@dataclass
class GetLocationUseCase:
    def execute(self, location_id) -> LocationSchema:
        return LocationSchema(
            coordinate=None,
            country="Japan",
            state="Chiyoda City",
            city="Tokyo",
            street_address="1-1 Chiyoda",
            zip_code="100-0001",
        )
