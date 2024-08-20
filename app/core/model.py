from contextlib import suppress
from datetime import datetime
from typing import Annotated
from uuid import UUID

from sqlalchemy import MetaData, inspect, text
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column


class Base(DeclarativeBase):
    # Integration of Naming Conventions into Operations, Autogenerate (for alembic)
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


class DataclassBase(MappedAsDataclass, Base, kw_only=True):
    __abstract__ = True

    # Patch to give opportunity to define related objects by id or instance
    def __post_init__(self) -> None:
        for relation in inspect(self).mapper.relationships:
            if getattr(self, relation.key) is None:
                with suppress(AttributeError):
                    delattr(self, relation.key)


UUID_PK = Annotated[UUID, mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))]
DATETIME_CREATED = Annotated[datetime, mapped_column(server_default=text("now()"))]
DATETIME_UPDATED = Annotated[datetime, mapped_column(server_default=text("now()"), onupdate=text("now()"))]


"""
location_key,latitude,longitude
1511980,35.685365,139.753303
228558,3.096889,101.661623
"""
