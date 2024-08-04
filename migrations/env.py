from collections.abc import Iterable
from logging.config import fileConfig
from uuid import uuid4

from alembic import context
from alembic.operations.ops import MigrationScript
from alembic.runtime.migration import MigrationContext
from alembic.script import ScriptDirectory
from sqlalchemy import create_engine, pool

from app.core.model import Base
from app.core.repository.sql import get_settings
from tools.load_db_models import load_db_models

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
load_db_models()
target_metadata = [Base.metadata]


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def process_revision_directives(
    context: MigrationContext,
    revision: Iterable,
    directives: list[MigrationScript],
) -> None:
    migration_script = directives[0]
    head_revision = ScriptDirectory.from_config(context.config).get_current_head()  # type: ignore
    if head_revision is None:
        new_rev_id = 1
    else:
        last_rev_id = int(head_revision.split("ver")[0].lstrip("0"))
        new_rev_id = last_rev_id + 1
    migration_script.rev_id = "ver".join([f"{new_rev_id:04}", str(uuid4()).replace("-", "")[:8]])


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    url = config.get_main_option("sqlalchemy.url", get_settings().dsn)
    engine = create_engine(url, pool_pre_ping=True, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            transactional_ddl=True,  # use ddl operation inside a transaction
            transaction_per_migration=True,  # each migration included into a separate transaction
            process_revision_directives=process_revision_directives,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
