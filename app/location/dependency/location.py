from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.repository.sql import get_session
from app.location.interface import ILocationRepository
from app.location.repository import LocationRepository


def get_location_repository(
    session: Session = Depends(get_session),
) -> ILocationRepository:
    return LocationRepository(session)
