import pytest
from pytest_mock import MockFixture

from app.core.repository import UnitOfWork
from app.location.client import ILocationClient
from app.location.domain import Location
from app.location.interface import ILocationRepository
from app.location.web import CreateLocationDTO, UpdateLocationDTO
from app.location.web.route import create_location, delete_location, get_location, update_location


def test_create_location_should_create_and_return_location(
    execute_create_location_use_case_mock: MockFixture,
    location: Location,
    create_location_dto: CreateLocationDTO,
    location_repository: ILocationRepository,
    location_client: ILocationClient,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    execute_create_location_use_case_mock.return_value = location
    # Act
    create_location_response = create_location(create_location_dto, unit_of_work, location_repository, location_client)
    # Assert
    assert create_location_response is not None


def test_get_location_should_return_location(
    execute_get_location_use_case_mock: MockFixture,
    location: Location,
    location_repository: ILocationRepository,
) -> None:
    # Arrange
    execute_get_location_use_case_mock.return_value = location
    # Act
    get_location_response = get_location(location.id, location_repository)
    # Assert
    assert get_location_response is not None


def test_update_location_should_return_update_and_return_location(
    execute_update_location_use_case_mock: MockFixture,
    location: Location,
    update_location_dto: UpdateLocationDTO,
    location_repository: ILocationRepository,
    location_client: ILocationClient,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    execute_update_location_use_case_mock.return_value = location
    # Act
    update_location_response = update_location(
        location.id, update_location_dto, unit_of_work, location_repository, location_client
    )
    # Assert
    assert update_location_response is not None


def test_delete_location_should_delete_location(
    execute_delete_location_use_case_mock: MockFixture,
    location: Location,
    location_repository: ILocationRepository,
    unit_of_work: UnitOfWork,
) -> None:
    # Arrange
    execute_delete_location_use_case_mock.return_value = None
    # Act
    delete_location_response = delete_location(location.id, unit_of_work, location_repository)
    # Assert
    assert delete_location_response is None


@pytest.fixture
def execute_create_location_use_case_mock(
    mocker: MockFixture,
) -> MockFixture:
    return mocker.patch("app.location.web.route.CreateLocationUseCase.execute")


@pytest.fixture
def execute_get_location_use_case_mock(
    mocker: MockFixture,
) -> MockFixture:
    return mocker.patch("app.location.web.route.GetLocationUseCase.execute")


@pytest.fixture
def execute_update_location_use_case_mock(
    mocker: MockFixture,
) -> MockFixture:
    return mocker.patch("app.location.web.route.UpdateLocationUseCase.execute")


@pytest.fixture
def execute_delete_location_use_case_mock(
    mocker: MockFixture,
) -> MockFixture:
    return mocker.patch("app.location.web.route.DeleteLocationUseCase.execute")
