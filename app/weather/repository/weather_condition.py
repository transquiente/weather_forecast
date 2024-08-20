from sqlalchemy.orm import joinedload

from app.core.repository.sql import BaseRepository
from app.weather.domain import WeatherCondition
from app.weather.interface import IWeatherConditionRepository


class WeatherConditionRepository(BaseRepository, IWeatherConditionRepository):
    model = WeatherCondition

    base_options = [
        joinedload(WeatherCondition.location).noload("*"),
    ]
