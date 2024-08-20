from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal

from app.location.client.schema import LocationClientLocationSchema


@dataclass
class ILocationClient(ABC):
    @abstractmethod
    def get_location(self, latitude: Decimal, longitude: Decimal) -> LocationClientLocationSchema:
        raise NotImplementedError
