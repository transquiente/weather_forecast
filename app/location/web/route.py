from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.core.repository.sql import UnitOfWork, get_uow
from app.core.schema import ErrorMessageSchema
from app.location.client import ILocationClient
from app.location.dependency import get_location_client, get_location_repository
from app.location.domain import Location
from app.location.interface import ILocationRepository
from app.location.use_case import (
    CreateLocationUseCase,
    DeleteLocationUseCase,
    GetLocationUseCase,
    UpdateLocationUseCase,
)
from app.location.web.dto import CreateLocationDTO, UpdateLocationDTO
from app.location.web.schema import LocationSchema

router = APIRouter(prefix="/location", tags=["Location"])


@router.post(
    "",
    response_model=LocationSchema,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorMessageSchema}},
)
def create_location(
    location_dto: CreateLocationDTO,
    uow: UnitOfWork = Depends(get_uow),
    location_repository: ILocationRepository = Depends(get_location_repository),
    location_client: ILocationClient = Depends(get_location_client),
) -> Location:
    use_case = CreateLocationUseCase(uow, location_repository, location_client)
    return use_case.execute(location_dto)


@router.get(
    "/{location_id}",
    status_code=status.HTTP_200_OK,
    response_model=LocationSchema,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageSchema}},
)
def get_location(
    location_id: UUID,
    location_repository: ILocationRepository = Depends(get_location_repository),
) -> LocationSchema:
    use_case = GetLocationUseCase(location_repository)
    return use_case.execute(location_id)


@router.patch(
    "/{location_id}",
    status_code=status.HTTP_200_OK,
    response_model=LocationSchema,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorMessageSchema},
        status.HTTP_404_NOT_FOUND: {"model": ErrorMessageSchema},
    },
)
def update_location(
    location_id: UUID,
    location_dto: UpdateLocationDTO,
    uow: UnitOfWork = Depends(get_uow),
    location_repository: ILocationRepository = Depends(get_location_repository),
    location_client: ILocationClient = Depends(get_location_client),
) -> Location:
    use_case = UpdateLocationUseCase(uow, location_repository, location_client)
    return use_case.execute(location_id, location_dto)


@router.delete(
    "/{location_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageSchema}},
)
def delete_location(
    location_id: UUID,
    uow: UnitOfWork = Depends(get_uow),
    location_repository: ILocationRepository = Depends(get_location_repository),
) -> None:
    use_case = DeleteLocationUseCase(uow, location_repository)
    return use_case.execute(location_id)
