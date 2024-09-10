import pytest
from sqlalchemy.orm import Session

from app.location.interface import ILocationRepository
from app.location.repository import LocationRepository


@pytest.fixture
def location_repository(db_session: Session) -> ILocationRepository:
    return LocationRepository(db_session)
