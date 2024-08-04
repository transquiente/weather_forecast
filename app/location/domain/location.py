from sqlalchemy.orm import Mapped, mapped_column

from app.core.model import DATETIME_CREATED, UUID_PK, DataclassBase


class Location(DataclassBase):
    __tablename__ = "location"
    id: Mapped[UUID_PK] = mapped_column(default=None)
    country: Mapped[str | None] = mapped_column(default=None)
    state: Mapped[str | None] = mapped_column(default=None)
    city: Mapped[str | None] = mapped_column(default=None)
    street_address: Mapped[str | None] = mapped_column(default=None)
    zip_code: Mapped[str | None] = mapped_column(default=None)
    created_at: Mapped[DATETIME_CREATED] = mapped_column(init=False)
