import pytest
from sqlalchemy.orm import Session

from app.weather.interface import IWeatherConditionRepository
from app.weather.repository import WeatherConditionRepository


@pytest.fixture
def weather_condition_repository(db_session: Session) -> IWeatherConditionRepository:
    return WeatherConditionRepository(db_session)
