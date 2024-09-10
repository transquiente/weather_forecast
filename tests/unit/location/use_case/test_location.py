from app.core.repository.sql import UnitOfWork
from app.location.client import ILocationClient
from app.location.domain.location import Location
from app.location.interface import ILocationRepository
from app.location.use_case import (
    CreateLocationUseCase,
    DeleteLocationUseCase,
    GetLocationUseCase,
    UpdateLocationUseCase,
)
from app.location.web.dto import CreateLocationDTO, UpdateLocationDTO
from app.location.web.schema import LocationSchema
from tests.unit.location.fixtures import LocationFactory


def test_create_location_use_case_calls_repository_correctly(
    location: Location,
    create_location_dto: CreateLocationDTO,
    location_repository: ILocationRepository,
    location_client: ILocationClient,
    location_client_location_schema: LocationSchema,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    def add_id(obj: Location) -> Location:
        obj.id = location.id
        return obj

    location_client.get_location.return_value = location_client_location_schema
    location_repository.get.return_value = location
    location_repository.add.side_effect = lambda obj: add_id(obj)
    use_case = CreateLocationUseCase(
        unit_of_work,
        location_repository,
        location_client,
    )
    # Act
    use_case.execute(create_location_dto)
    # Assert
    location_client.get_location.assert_called_once()
    location_repository.add.assert_called_once()
    location_repository.get.assert_called_once_with(location.id, load_refreshed=True)


def test_get_location_use_case_calls_repository_correctly(
    location: Location,
    location_repository: ILocationRepository,
) -> None:
    # Arrange
    location_repository.get.return_value = location
    use_case = GetLocationUseCase(location_repository)
    # Act
    use_case.execute(location.id)
    # Assert
    location_repository.get.assert_called_once_with(location.id)


def test_update_location_use_case_calls_repository_correctly(
    update_location_dto: UpdateLocationDTO,
    location_factory: type[LocationFactory],
    location_repository: ILocationRepository,
    location_client: ILocationClient,
    location_client_location_schema: LocationSchema,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    location = location_factory()
    location_client.get_location.return_value = location_client_location_schema
    location_repository.get.return_value = location
    use_case = UpdateLocationUseCase(
        unit_of_work,
        location_repository,
        location_client,
    )
    # Act
    use_case.execute(location.id, update_location_dto)
    # Assert
    location_client.get_location.assert_called_once()
    location_repository.add.assert_called_once()
    assert location_repository.get.call_count == 2


def test_delete_location_use_case_calls_repository_correctly(
    location: Location,
    location_repository: ILocationRepository,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    location_repository.get.return_value = location
    use_case = DeleteLocationUseCase(unit_of_work, location_repository)
    # Act
    use_case.execute(location.id)
    # Assert
    location_repository.get.assert_called_once_with(location.id)
    location_repository.delete.assert_called_once_with(location)
