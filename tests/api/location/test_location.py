from collections.abc import Callable

from fastapi.encoders import jsonable_encoder
from httpx import Client
from sqlalchemy.orm import Session

from app.core.constants import APP_VERSION_PREFIX
from app.location.client import ILocationClient, LocationClientLocationSchema
from app.location.web import CreateLocationDTO


def test_create_location_should_create_location(
    location_client: ILocationClient,
    location_client_location_schema: LocationClientLocationSchema,
    create_location_dto: CreateLocationDTO,
    client: Client,
    db_session: Session,
    prepare_db: Callable,
) -> None:
    # Arrange
    prepare_db()
    location_client.get_location.return_value = location_client_location_schema
    # Act
    response = client.post(f"{APP_VERSION_PREFIX}/location", json=jsonable_encoder(create_location_dto))
    # Assert
    assert response.status_code == 201
