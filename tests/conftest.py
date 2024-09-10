import os
from argparse import Namespace
from contextlib import contextmanager
from logging import getLogger
from types import SimpleNamespace
from uuid import uuid4

import pytest
from alembic.command import upgrade
from alembic.config import Config
from sqlalchemy import Engine, create_engine
from sqlalchemy_utils import create_database, drop_database
from yarl import URL

from app.core.repository import get_settings
from tools.load_db_models import load_db_models

load_db_models()

logger = getLogger(__name__)


APP_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def make_alembic_config(cmd_opts: Namespace | SimpleNamespace, base_path: str = APP_ROOT_PATH) -> Config:
    # Replace path to alembic.ini file to absolute
    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = os.path.join(base_path, cmd_opts.config)

    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name, cmd_opts=cmd_opts)

    # Replace path to alembic folder to absolute
    alembic_location = config.get_main_option("script_location")
    if not os.path.isabs(alembic_location):
        config.set_main_option("script_location", os.path.join(base_path, alembic_location))
    if cmd_opts.pg_url:
        config.set_main_option("sqlalchemy.url", cmd_opts.pg_url)

    return config


def alembic_config_from_url(pg_url: str | None = None) -> Config:
    """
    Provides Python object, representing alembic.ini file.
    """
    cmd_options = SimpleNamespace(
        config="alembic.ini",
        name="alembic",
        pg_url=pg_url,
        raiseerr=False,
        x=None,
    )

    return make_alembic_config(cmd_options)


@contextmanager
def tmp_database(db_url: URL, suffix: str = "", project_name=__name__, **kwargs) -> str:
    tmp_db_name = ".".join([uuid4().hex, project_name, suffix])
    tmp_db_url = str(db_url.with_path(tmp_db_name))
    create_database(tmp_db_url, **kwargs)
    try:
        yield tmp_db_url
    finally:
        drop_database(tmp_db_url)


@pytest.fixture(scope="session")
def pg_url() -> URL:
    """
    Provides base PostgreSQL URL for creating temporary databases.
    """
    return URL(get_settings().dsn)


@pytest.fixture
def postgres(pg_url: URL) -> str:
    """
    Creates empty temporary database.
    """
    with tmp_database(pg_url, "pytest") as tmp_url:
        yield tmp_url


@pytest.fixture()
def alembic_config(postgres: str) -> Config:
    """
    Alembic configuration object, bound to temporary database.
    """
    return alembic_config_from_url(postgres)


@pytest.fixture()
def postgres_engine(postgres: str) -> Engine:
    """
    SQLAlchemy engine, bound to temporary database.
    """
    engine = create_engine(postgres, echo=True)
    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture(scope="session")
def migrated_postgres_template(pg_url: URL) -> str:
    """
    Creates temporary database and applies migrations.
    Database can be used as template to fast creation databases for tests.

    Has "session" scope, so is called only once per tests run.
    """
    with tmp_database(pg_url, "template") as tmp_url:
        alembic_config = alembic_config_from_url(tmp_url)
        upgrade(alembic_config, "head")
        yield tmp_url


@pytest.fixture(scope="session")
def migrated_postgres(
    pg_url: URL,
    migrated_postgres_template: str,
) -> str:
    """
    Quickly creates migrated database with initial data using temporary database as base.
    Use this fixture in tests that require migrated database.
    """
    template_db = URL(migrated_postgres_template).name
    with tmp_database(pg_url, suffix="migrated", template=template_db) as tmp_url:
        engine = create_engine(tmp_url)
        engine.dispose()
        yield tmp_url


@pytest.fixture
def prepared_postgres(pg_url: URL, migrated_postgres: str) -> str:
    template_db = URL(migrated_postgres).name
    with tmp_database(pg_url, suffix="pytest", template=template_db) as tmp_url:
        yield tmp_url


@pytest.fixture
def prepared_postgres_engine(prepared_postgres: str) -> Engine:
    """
    SQLAlchemy engine, bound to migrated temporary database.
    """
    engine = create_engine(prepared_postgres, pool_pre_ping=True, pool_size=10, max_overflow=15, pool_recycle=3600)
    try:
        yield engine
    finally:
        engine.dispose()
