from app.core.schema import BaseSchema


class GetWeatherCurrentConditionWeatherClientDTO(BaseSchema):
    apikey: str
    language: str = "en-us"
    details: bool = False


class GetWeatherForecastConditionWeatherClientDTO(GetWeatherCurrentConditionWeatherClientDTO):
    metric: bool = False
