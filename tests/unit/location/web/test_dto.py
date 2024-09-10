from app.location.client import LocationClientLocationSchema
from app.location.domain import Location
from app.location.web import CreateLocationDTO, UpdateLocationDTO


def test_create_location_dto_from_location_should_return_location(
    location: Location,
    create_location_dto: CreateLocationDTO,
    location_client_location_schema: LocationClientLocationSchema,
) -> None:
    # Act
    location_from_dto = create_location_dto.from_dto(location_client_location_schema)
    # Assert
    assert location_from_dto is not None


def test_update_location_dto_should_return_location(
    location: Location,
    update_location_dto: UpdateLocationDTO,
    location_client_location_schema: LocationClientLocationSchema,
) -> None:
    # Act
    updated_location_from_dto = update_location_dto.update_from_dto(location, location_client_location_schema)
    # Assert
    assert updated_location_from_dto is not None
