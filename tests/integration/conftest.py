from collections.abc import Callable, Generator

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from tests.integration.core.fixtures.unit_of_work import unit_of_work  # noqa: F401
from tests.integration.location.fixtures import location_repository  # noqa: F401
from tests.integration.weather.fixtures import weather_condition_repository  # noqa: F401


@pytest.fixture(autouse=True)
def db_engine(prepared_postgres_engine: Engine) -> Generator[Engine, None, None]:
    yield prepared_postgres_engine


@pytest.fixture
def session_maker(db_engine: Engine) -> Callable[[], Session]:
    return sessionmaker(db_engine, expire_on_commit=False)


@pytest.fixture
def db_session(session_maker: Callable[[], Session]) -> Generator[Session, None]:
    with session_maker() as session:
        yield session


@pytest.fixture
def prepare_db(db_session: Session) -> Callable:
    def _prepare_db():
        db_session.commit()
        db_session.expunge_all()

    return _prepare_db
