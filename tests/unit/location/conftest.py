from pytest_factoryboy import register

from tests.unit.core.conftest import unit_of_work  # noqa: F401
from tests.unit.location.fixtures import (  # noqa: F401
    LocationFactory,
    create_location_dto,
    location,
    location_client,
    location_client_location_schema,
    location_repository,
    update_location_dto,
)

register(LocationFactory)
