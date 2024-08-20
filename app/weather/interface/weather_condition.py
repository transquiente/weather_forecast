from abc import ABC

from app.core.repository.sql import IBaseRepository
from app.weather.domain import WeatherCondition


class IWeatherConditionRepository(IBaseRepository[WeatherCondition], ABC):
    pass
