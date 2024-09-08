from pytest_factoryboy import register

from tests.integration.core.fixtures import unit_of_work  # noqa: F401
from tests.integration.location.fixtures import location_repository  # noqa: F401
from tests.unit.conftest import LocationFactory, location  # noqa: F401

register(LocationFactory)
