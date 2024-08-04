from app.core.repository.sql import BaseRepository
from app.location.domain import Location
from app.location.interface import ILocationRepository


class LocationRepository(BaseRepository, ILocationRepository):
    model = Location
    base_options = []
