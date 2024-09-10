from decimal import Decimal
from itertools import count

import pytest
from pytest_mock import MockerFixture

from app.location.client import ILocationClient, LocationClientLocationSchema

counter = count()


@pytest.fixture
def location_client(mocker: MockerFixture) -> ILocationClient:
    return mocker.Mock(spec=ILocationClient)


@pytest.fixture
def location_client_location_schema() -> LocationClientLocationSchema:
    number = next(counter)
    key = f"location_{number}"
    return LocationClientLocationSchema(
        **{
            "Key": key,
            "EnglishName": key.capitalize(),
            "PrimaryPostalCode": "457-213",
            "Country": {
                "ID": f"test_{number}",
                "EnglishName": key.capitalize(),
            },
            "AdministrativeArea": {
                "ID": f"test_{number}",
                "EnglishName": key.capitalize(),
                "EnglishType": "General",
            },
            "GeoPosition": {
                "Latitude": Decimal("93.7621"),
                "Longitude": Decimal("50.4576"),
                "Elevation": {"Metric": {"Value": Decimal("13.879")}},
            },
        }
    )
