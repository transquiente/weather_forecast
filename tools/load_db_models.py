from sqlalchemy.orm import configure_mappers


def load_db_models():
    from app.location.domain import Location  # noqa: F401

    configure_mappers()
