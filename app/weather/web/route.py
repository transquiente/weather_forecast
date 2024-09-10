from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.core.repository.sql import UnitOfWork, get_uow
from app.core.schema import ErrorMessageSchema
from app.location.dependency import get_location_repository
from app.location.interface import ILocationRepository
from app.weather.client import IWeatherClient
from app.weather.constant import WeatherDataType
from app.weather.dependency import get_weather_client, get_weather_condition_repository
from app.weather.domain import WeatherCondition
from app.weather.interface import IWeatherConditionRepository
from app.weather.use_case import (
    AddCurrentWeatherConditionUseCase,
    AddForecastWeatherConditionUseCase,
    GetWeatherConditionUseCase,
)
from app.weather.web.dto import WeatherConditionDTO
from app.weather.web.schema import WeatherSchema

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.post(
    "",
    response_model=WeatherSchema,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorMessageSchema}},
)
def add_weather_condition(
    weather_condition_dto: WeatherConditionDTO,
    uow: UnitOfWork = Depends(get_uow),
    weather_condition_repository: IWeatherConditionRepository = Depends(get_weather_condition_repository),
    location_repository: ILocationRepository = Depends(get_location_repository),
    weather_client: IWeatherClient = Depends(get_weather_client),
) -> WeatherCondition:
    if weather_condition_dto.data_type == WeatherDataType.CURRENT_CONDITION:
        use_case = AddCurrentWeatherConditionUseCase(  # type: ignore
            uow, location_repository, weather_condition_repository, weather_client
        )
    else:
        use_case = AddForecastWeatherConditionUseCase(  # type: ignore
            uow, location_repository, weather_condition_repository, weather_client
        )
    return use_case.execute(weather_condition_dto)


@router.get(
    "/{weather_condition_id}",
    status_code=status.HTTP_200_OK,
    response_model=WeatherSchema,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageSchema}},
)
def get_weather_condition_for_location(
    weather_condition_id: UUID,
    weather_condition_repository: IWeatherConditionRepository = Depends(get_weather_condition_repository),
) -> WeatherCondition:
    use_case = GetWeatherConditionUseCase(weather_condition_repository)
    return use_case.execute(weather_condition_id)
