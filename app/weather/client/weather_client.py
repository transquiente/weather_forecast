from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

import httpx
from fastapi import status
from pydantic_settings import BaseSettings

from app.weather.client.dto import (
    GetWeatherCurrentConditionWeatherClientDTO,
    GetWeatherForecastConditionWeatherClientDTO,
)
from app.weather.client.exception import (
    WeatherClientBadRequestException,
    WeatherClientBaseException,
    WeatherClientInvalidApiKeyException,
    WeatherClientNotFoundException,
    WeatherClientRequestsExceededException,
)
from app.weather.client.interface import IWeatherClient
from app.weather.client.schema import (
    WeatherClientWeatherCurrentConditionSchema,
    WeatherClientWeatherForecastConditionSchema,
)


class WeatherClientSettings(BaseSettings):
    api_key: str = ""
    base_url: str = ""

    class Config:
        env_prefix = "weather_"


def get_weather_client_settings() -> WeatherClientSettings:
    return WeatherClientSettings()


@dataclass
class WeatherClient(IWeatherClient):
    settings: WeatherClientSettings
    api_key: str = field(init=False)
    base_url: str = field(init=False)
    current_condition_url: str = field(init=False, default="currentconditions/v1")
    twelve_hour_forecast_url: str = field(init=False, default="forecasts/v1/hourly/12hour")

    def __post_init__(self) -> None:
        self.api_key = self.settings.api_key
        self.base_url = self.settings.base_url

    def get_current_weather_condition_for_location(
        self,
        location_key: str,
        details: bool = False,
    ) -> WeatherClientWeatherCurrentConditionSchema:
        current_condition_dto = GetWeatherCurrentConditionWeatherClientDTO(
            apikey=self.api_key,
            details=details,
        )
        response_json = self._make_request(
            method="GET",
            url=f"{self.base_url}/{self.current_condition_url}/{location_key}",
            params=current_condition_dto.model_dump(mode="json"),
        )
        current_weather_condition = response_json[0]
        response: WeatherClientWeatherCurrentConditionSchema = (
            WeatherClientWeatherCurrentConditionSchema.model_validate(current_weather_condition)
        )
        return response

    def get_weather_forecast_for_location(
        self,
        location_key: str,
        details: bool = False,
        metric: bool = False,
    ) -> WeatherClientWeatherForecastConditionSchema:
        forecast_condition_dto = GetWeatherForecastConditionWeatherClientDTO(
            apikey=self.api_key,
            details=details,
            metric=metric,
        )
        response_json = self._make_request(
            method="GET",
            url=f"{self.base_url}/{self.twelve_hour_forecast_url}/{location_key}",
            params=forecast_condition_dto.model_dump(mode="json"),
        )
        response = [
            WeatherClientWeatherForecastConditionSchema.model_validate(weather_condition)
            for weather_condition in response_json
        ]
        next_date_time = datetime.now(timezone.utc) + timedelta(hours=1)
        next_hour_forecast: WeatherClientWeatherForecastConditionSchema = next(
            filter(
                lambda x: x.date_time.hour == next_date_time.hour and x.date_time.day == next_date_time.day, response
            ),
            response[0],
        )
        return next_hour_forecast

    def _make_request(self, method: str, url: str, **kwargs) -> list:
        try:
            with httpx.Client() as client:
                response = client.request(method=method, url=url, **kwargs)
            return self._handle_response(response)
        except Exception as exc:
            if isinstance(exc, WeatherClientBaseException):
                raise exc from exc
            raise WeatherClientBaseException(str(exc), response={"error": exc.__class__.__name__}) from exc

    def _handle_response(self, response: httpx.Response) -> list:
        if response.status_code == status.HTTP_200_OK:
            response_json: list[dict] = response.json()
            return response_json
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise WeatherClientBadRequestException("Weather client received Bad Request response")
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise WeatherClientInvalidApiKeyException("Wrong credentials for weather client")
        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise WeatherClientNotFoundException("Url not found for weather client")
        raise WeatherClientRequestsExceededException("Too many requests to weather client")
