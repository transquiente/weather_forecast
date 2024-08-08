from functools import cache

from pydantic_settings import BaseSettings


class CORSSettings(BaseSettings):
    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True

    class Config:
        env_prefix = "cors_"


@cache
def get_cors_settings() -> CORSSettings:
    return CORSSettings()
