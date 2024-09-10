from dataclasses import dataclass
from uuid import UUID

from app.core.repository.sql import UnitOfWork
from app.location.client import ILocationClient
from app.location.interface import ILocationRepository
from app.location.web.dto import CreateLocationDTO, UpdateLocationDTO
from app.location.web.schema import LocationSchema


@dataclass
class CreateLocationUseCase:
    uow: UnitOfWork
    location_repository: ILocationRepository
    location_client: ILocationClient

    def execute(self, location_dto: CreateLocationDTO) -> LocationSchema:
        location_from_location_client = self.location_client.get_location(
            latitude=location_dto.latitude,
            longitude=location_dto.longitude,
        )
        with self.uow:
            location = location_dto.from_dto(location_from_location_client)
            self.location_repository.add(location)
        location = self.location_repository.get(location.id, load_refreshed=True)
        location_schema: LocationSchema = LocationSchema.model_validate(location)
        return location_schema


@dataclass
class GetLocationUseCase:
    location_repository: ILocationRepository

    def execute(self, location_id: UUID) -> LocationSchema:
        location = self.location_repository.get(location_id)
        location_schema: LocationSchema = LocationSchema.model_validate(location)
        return location_schema


@dataclass
class UpdateLocationUseCase:
    uow: UnitOfWork
    location_repository: ILocationRepository
    location_client: ILocationClient

    def execute(self, location_id: UUID, location_dto: UpdateLocationDTO) -> LocationSchema:
        updated_location_from_location_client = None
        location = self.location_repository.get(location_id)
        if (
            location_dto.latitude is not None
            and location_dto.longitude is not None
            and (location_dto.latitude != location.latitude or location_dto.longitude != location.longitude)
        ):
            updated_location_from_location_client = self.location_client.get_location(
                latitude=location_dto.latitude,
                longitude=location_dto.longitude,
            )
        with self.uow:
            location = location_dto.update_from_dto(location, updated_location_from_location_client)
            self.location_repository.add(location)
        location = self.location_repository.get(location.id, load_refreshed=True)
        location_schema: LocationSchema = LocationSchema.model_validate(location)
        return location_schema


@dataclass
class DeleteLocationUseCase:
    uow: UnitOfWork
    location_repository: ILocationRepository

    def execute(self, location_id) -> None:
        location = self.location_repository.get(location_id)
        with self.uow:
            self.location_repository.delete(location)
