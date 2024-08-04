from fastapi import APIRouter, FastAPI

from app.core.constants import APP_VERSION_PREFIX
from app.core.repository.sql.db import session_maker_factory
from app.location.web import router as location_router

v01_router = APIRouter(prefix=APP_VERSION_PREFIX)


def configure_app(app: FastAPI) -> None:
    do_app_core_configuration(app)
    configure_routes(app)


def do_app_core_configuration(app: FastAPI) -> None:
    app.state.session_maker = session_maker_factory()


def configure_routes(app: FastAPI) -> None:
    routes = [
        location_router,
    ]
    for route in routes:
        v01_router.include_router(route)

    app.include_router(v01_router)


def create_app() -> FastAPI:
    app = FastAPI()
    configure_app(app)
    return app
