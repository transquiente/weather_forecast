from fastapi import APIRouter, FastAPI

from app.core.constants import APP_VERSION_PREFIX
from app.core.repository.sql import session_maker_factory
from app.core.web import configure_cors, configure_error_handlers
from app.location.web import router as location_router
from app.weather.web import router as weather_router

v01_router = APIRouter(prefix=APP_VERSION_PREFIX)


def configure_app(app: FastAPI) -> None:
    do_app_core_configuration(app)
    configure_routes(app)


def do_app_core_configuration(app: FastAPI) -> None:
    app.state.session_maker = session_maker_factory()
    configure_cors(app)
    configure_error_handlers(app)


def configure_routes(app: FastAPI) -> None:
    routes = [
        location_router,
        weather_router,
    ]
    for route in routes:
        v01_router.include_router(route)

    app.include_router(v01_router)


def create_app() -> FastAPI:
    app = FastAPI()
    configure_app(app)
    return app
