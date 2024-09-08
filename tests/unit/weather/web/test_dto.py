from app.weather.client import WeatherClientWeatherCurrentConditionSchema, WeatherClientWeatherForecastConditionSchema
from app.weather.domain import WeatherCondition
from app.weather.web import WeatherConditionDTO


def test_current_weather_condition_dto_from_dto_should_return_weather_condition(
    current_condition_weather_condition_dto: WeatherConditionDTO,
    weather_client_weather_current_condition_schema: WeatherClientWeatherCurrentConditionSchema,
) -> None:
    # Act
    weather_condition_from_dto = current_condition_weather_condition_dto.from_dto(
        weather_client_weather_current_condition_schema
    )
    # Assert
    assert weather_condition_from_dto is not None
    assert isinstance(weather_condition_from_dto, WeatherCondition)


def test_forecast_weather_condition_dto_from_dto_should_return_weather_condition(
    forecast_condition_weather_condition_dto: WeatherConditionDTO,
    weather_client_weather_forecast_condition_schema: WeatherClientWeatherForecastConditionSchema,
) -> None:
    # Act
    weather_condition_from_dto = forecast_condition_weather_condition_dto.from_dto(
        weather_client_weather_forecast_condition_schema
    )
    # Assert
    assert weather_condition_from_dto is not None
    assert isinstance(weather_condition_from_dto, WeatherCondition)
