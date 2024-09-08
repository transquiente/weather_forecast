from uuid import uuid4

import factory
import pytest
from pytest_mock import MockerFixture

from app.location.domain import Location
from app.location.interface import ILocationRepository
from app.location.web import CreateLocationDTO, UpdateLocationDTO


@pytest.fixture
def location_repository(mocker: MockerFixture) -> ILocationRepository:
    return mocker.Mock(spec=ILocationRepository)


class LocationFactory(factory.Factory):
    class Meta:
        model = Location

    id = factory.LazyFunction(uuid4)
    country = factory.Faker("country")
    state = factory.Faker("state")
    city = factory.Faker("city")
    street_address = factory.Faker("street_address")
    zip_code = factory.Faker("zipcode")
    location_key = factory.Sequence(lambda x: f"location_key_{x}")
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
    weather_information = []


@pytest.fixture
def location(location_factory: type[LocationFactory]) -> Location:
    location = location_factory()
    return location


@pytest.fixture
def create_location_dto(location: Location) -> CreateLocationDTO:
    return CreateLocationDTO(
        country=location.country,
        state=location.state,
        city=location.city,
        street_address=location.street_address,
        zip_code=location.zip_code,
        latitude=location.latitude,
        longitude=location.longitude,
    )


@pytest.fixture
def update_location_dto(location: Location) -> UpdateLocationDTO:
    return UpdateLocationDTO(
        country=location.country,
        state=location.state,
        city=location.city,
        street_address=location.street_address,
        zip_code=location.zip_code,
        latitude=location.latitude,
        longitude=location.longitude,
    )
