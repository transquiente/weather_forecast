from sqlalchemy.orm import configure_mappers


def load_db_models():
    from app.weather.domain import WeatherCondition  # noqa: F401, I001
    from app.location.domain import Location  # noqa: F401, I001

    configure_mappers()
