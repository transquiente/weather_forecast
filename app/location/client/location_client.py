from dataclasses import dataclass, field
from decimal import Decimal

import httpx
from fastapi import status
from pydantic_settings import BaseSettings

from app.location.client.dto import GetLocationLocationClientDTO
from app.location.client.exception import (
    LocationClientBadRequestException,
    LocationClientBaseException,
    LocationClientInvalidApiKeyException,
    LocationClientNotFoundException,
    LocationClientRequestsExceededException,
)
from app.location.client.interface import ILocationClient
from app.location.client.schema import LocationClientLocationSchema


class LocationClientSettings(BaseSettings):
    api_key: str = ""
    base_url: str = ""

    class Config:
        env_prefix = "location_"


def get_location_client_settings() -> LocationClientSettings:
    return LocationClientSettings()


@dataclass
class LocationClient(ILocationClient):
    settings: LocationClientSettings
    api_key: str = field(init=False)
    base_url: str = field(init=False)
    location_url: str = field(init=False, default="locations/v1/cities/geoposition/search")

    def __post_init__(self) -> None:
        self.api_key = self.settings.api_key
        self.base_url = self.settings.base_url

    def get_location(self, latitude: Decimal, longitude: Decimal) -> LocationClientLocationSchema:
        dto = GetLocationLocationClientDTO(
            apikey=self.api_key,
            q=f"{latitude},{longitude}",
        )
        response_json = self._make_request(
            method="POST",
            url=f"{self.base_url}/{self.location_url}",
            params=dto.model_dump(mode="json"),
        )
        response: LocationClientLocationSchema = LocationClientLocationSchema.parse_obj(response_json)
        return response

    def _make_request(self, method: str, url: str, **kwargs) -> dict:
        try:
            with httpx.Client() as client:
                response = client.request(method=method, url=url, **kwargs)
            return self._handle_response(response)
        except Exception as exc:
            if isinstance(exc, LocationClientBaseException):
                raise exc from exc
            raise LocationClientBaseException(str(exc), response={"error": exc.__class__.__name__}) from exc

    def _handle_response(self, response: httpx.Response) -> dict:
        if response.status_code == status.HTTP_200_OK:
            response_json: dict = response.json()
            return response_json
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise LocationClientBadRequestException("Location client received Bad Request response")
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise LocationClientInvalidApiKeyException("Wrong credentials for location client")
        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise LocationClientNotFoundException("Url not found for location client")
        raise LocationClientRequestsExceededException("Too many requests to location client")
