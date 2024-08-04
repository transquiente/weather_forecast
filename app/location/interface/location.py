from abc import ABC

from app.core.repository.sql import IBaseRepository
from app.location.domain import Location


class ILocationRepository(IBaseRepository[Location], ABC):
    pass
