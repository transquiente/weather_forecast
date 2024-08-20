from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.model import DATETIME_CREATED, UUID_PK, DataclassBase

if TYPE_CHECKING:
    from app.weather.domain import WeatherCondition


class Location(DataclassBase):
    __tablename__ = "location"
    id: Mapped[UUID_PK] = mapped_column(default=None)

    country: Mapped[str | None] = mapped_column(default=None)
    state: Mapped[str | None] = mapped_column(default=None)
    city: Mapped[str | None] = mapped_column(default=None)
    street_address: Mapped[str | None] = mapped_column(default=None)
    zip_code: Mapped[str | None] = mapped_column(default=None)
    location_key: Mapped[str | None] = mapped_column(default=None)
    latitude: Mapped[Decimal | None] = mapped_column(default=None)
    longitude: Mapped[Decimal | None] = mapped_column(default=None)
    created_at: Mapped[DATETIME_CREATED] = mapped_column(init=False)

    weather_information: Mapped[list["WeatherCondition"]] = relationship(
        back_populates="location",
        cascade="all, delete-orphan",
        default_factory=list,
    )
