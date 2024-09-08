from app.core.repository import UnitOfWork
from app.location.domain import Location
from app.location.interface import ILocationRepository


def test_add_should_create_location_if_not_exists(
    location: Location,
    location_repository: ILocationRepository,
    unit_of_work: UnitOfWork,
) -> None:
    # Act
    with unit_of_work:
        location_repository.add(location)
        unit_of_work.commit()
    # Assert
    location_from_db = location_repository.get(location.id)
    assert location_from_db == location
    # Cleanup
    with unit_of_work:
        location_repository.delete(location_from_db)
        unit_of_work.commit()
