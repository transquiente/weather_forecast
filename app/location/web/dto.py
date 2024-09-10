from decimal import Decimal

from app.core.schema import BaseSchema
from app.location.client import LocationClientLocationSchema
from app.location.domain import Location


class CreateLocationDTO(BaseSchema):
    country: str | None
    state: str | None
    city: str | None
    street_address: str | None
    zip_code: str | None
    latitude: Decimal
    longitude: Decimal

    def from_dto(self, location: LocationClientLocationSchema | None) -> Location:
        l_country = location.country if location else None
        l_area = location.administrative_area if location else None
        l_geo_position = location.geo_position if location else None
        country = l_country.english_name if l_country else None
        state = " ".join([l_area.english_type, l_area.english_name]) if l_area else None
        return Location(
            country=self.country or country,
            state=self.state or state,
            city=self.city or location.english_name if location else None,
            street_address=self.street_address,
            zip_code=self.zip_code,
            latitude=self.latitude or l_geo_position.latitude if l_geo_position else None,
            longitude=self.longitude or l_geo_position.longitude if l_geo_position else None,
            location_key=location.key if location else None,
        )


class UpdateLocationDTO(CreateLocationDTO):
    def update_from_dto(
        self,
        location: Location,
        location_client_schema: LocationClientLocationSchema | None,
    ) -> Location:
        location_from_dto = self.from_dto(location_client_schema)
        location.country = location_from_dto.country or location.country
        location.state = location_from_dto.state or location.state
        location.city = location_from_dto.city or location.city
        location.street_address = location_from_dto.street_address or location.street_address
        location.zip_code = location_from_dto.zip_code or location.zip_code
        location.latitude = location_from_dto.latitude or location.latitude
        location.longitude = location_from_dto.longitude or location.longitude
        location.location_key = location_from_dto.location_key
        return location
