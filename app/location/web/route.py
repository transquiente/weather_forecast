from uuid import UUID

from fastapi import APIRouter

from app.location.use_case import GetLocationUseCase
from app.location.web.schema import LocationSchema

router = APIRouter(prefix="/location", tags=["Location"])


@router.get(
    "/{location_id}",
    response_model=LocationSchema
)
def get_inventory_item_details(
        location_id: UUID | None = None,
) -> LocationSchema:
    use_case = GetLocationUseCase()
    return use_case.execute(location_id)
