from app.core.repository import UnitOfWork
from app.weather.domain import WeatherCondition
from app.weather.interface import IWeatherConditionRepository


def test_add_should_add_weather_condition(
    current_weather_condition: WeatherCondition,
    weather_condition_repository: IWeatherConditionRepository,
    unit_of_work: UnitOfWork,
) -> None:
    # Act
    with unit_of_work:
        weather_condition_repository.add(current_weather_condition)
        unit_of_work.commit()
    # Assert
    weather_condition_from_db = weather_condition_repository.get(current_weather_condition.id)
    assert weather_condition_from_db == current_weather_condition
    # Cleanup
    with unit_of_work:
        weather_condition_repository.delete(weather_condition_from_db)
        unit_of_work.commit()
