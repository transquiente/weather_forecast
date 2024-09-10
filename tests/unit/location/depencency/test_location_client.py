from app.location.client import ILocationClient, get_location_client_settings
from app.location.dependency import get_location_client


def test_get_location_client_returns_location_client():
    assert isinstance(get_location_client(settings=get_location_client_settings()), ILocationClient)
