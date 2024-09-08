from app.location.dependency import get_location_repository
from app.location.interface import ILocationRepository


def test_get_location_repository_returns_location_repository():
    assert isinstance(get_location_repository(), ILocationRepository)
