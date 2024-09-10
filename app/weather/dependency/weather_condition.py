from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.repository.sql import get_session
from app.weather.interface import IWeatherConditionRepository
from app.weather.repository import WeatherConditionRepository


def get_weather_condition_repository(
    session: Session = Depends(get_session),
) -> IWeatherConditionRepository:
    return WeatherConditionRepository(session)
