from app.location.domain import Location
from app.location.web import LocationSchema


def test_location_schema_parse_location_without_errors(location: Location) -> None:
    # Act
    location_schema = LocationSchema.model_validate(location)
    # Assert
    assert location_schema is not None
