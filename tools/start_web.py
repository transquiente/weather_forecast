from fastapi import APIRouter, FastAPI

from app.core.constants import APP_VERSION_PREFIX
from app.location.web.route import router as location_router

v01_router = APIRouter(prefix=APP_VERSION_PREFIX)


def configure_app(app: FastAPI) -> None:
    configure_routes(app)


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
