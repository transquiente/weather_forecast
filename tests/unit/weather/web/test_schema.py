from app.weather.domain import WeatherCondition
from app.weather.web import WeatherSchema


def test_weather_schema_parse_current_weather_condition_without_errors(
    current_weather_condition: WeatherCondition,
) -> None:
    # Act
    weather_schema = WeatherSchema.model_validate(current_weather_condition)
    # Assert
    assert weather_schema is not None


def test_weather_schema_parse_forecast_weather_condition_without_errors(
    forecast_weather_condition: WeatherCondition,
) -> None:
    # Act
    weather_schema = WeatherSchema.model_validate(forecast_weather_condition)
    # Assert
    assert weather_schema is not None
