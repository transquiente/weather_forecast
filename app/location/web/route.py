from uuid import UUID

from fastapi import APIRouter, Depends

from app.location.dependency import get_location_repository
from app.location.interface import ILocationRepository
from app.location.use_case import GetLocationUseCase
from app.location.web.schema import LocationSchema

router = APIRouter(prefix="/location", tags=["Location"])


@router.get("/{location_id}", response_model=LocationSchema)
def get_inventory_item_details(
    location_id: UUID | None = None,
    location_repository: ILocationRepository = Depends(get_location_repository),
) -> LocationSchema:
    use_case = GetLocationUseCase(location_repository)
    return use_case.execute(location_id)
