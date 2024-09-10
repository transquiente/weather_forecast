from collections.abc import Callable

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Client
from pytest_factoryboy import register
from sqlalchemy.orm import Session

from app.location.client import LocationClient
from app.location.dependency import get_location_client
from app.weather.client import WeatherClient
from app.weather.dependency import get_weather_client
from tests.integration.conftest import (  # noqa: F401
    db_engine,
    db_session,
    location_repository,
    prepare_db,
    session_maker,
    weather_condition_repository,
)
from tests.unit.conftest import (  # noqa: F401
    LocationFactory,
    WeatherConditionFactory,
    create_location_dto,
    current_condition_weather_condition_dto,
    current_weather_condition,
    forecast_condition_weather_condition_dto,
    forecast_weather_condition,
    location,
    location_client,
    location_client_location_schema,
    update_location_dto,
    weather_client,
    weather_client_weather_current_condition_schema,
    weather_client_weather_forecast_condition_schema,
)
from tools.start_web import configure_app

register(LocationFactory)
register(WeatherConditionFactory)


@pytest.fixture(scope="session")
def global_app() -> FastAPI:
    app = FastAPI()
    configure_app(app)
    return app


@pytest.fixture
def app(
    global_app: FastAPI,
    session_maker: Callable[[], Session],  # noqa: F811
    location_client: LocationClient,  # noqa: F811
    weather_client: WeatherClient,  # noqa: F811
) -> FastAPI:
    global_app.dependency_overrides = {}
    global_app.state.session_maker = session_maker
    global_app.dependency_overrides[get_location_client] = lambda: location_client
    global_app.dependency_overrides[get_weather_client] = lambda: weather_client
    return global_app


@pytest.fixture
def client(app: FastAPI) -> Client:
    return TestClient(app)
