from fastapi import Depends

from app.location.client import ILocationClient, LocationClient, LocationClientSettings, get_location_client_settings


def get_location_client(
    settings: LocationClientSettings = Depends(get_location_client_settings),
) -> ILocationClient:
    return LocationClient(settings)
