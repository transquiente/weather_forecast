from uuid import UUID

from app.core.schema import BaseSchema
from app.weather.client import WeatherClientWeatherCurrentConditionSchema, WeatherClientWeatherForecastConditionSchema
from app.weather.constant import (
    PrecipitationIntensity,
    PrecipitationType,
    PrecipitationUnit,
    SolarIrradianceUnit,
    TemperatureUnit,
    WeatherDataType,
    WindDirection,
    WindSpeedUnit,
)
from app.weather.domain import WeatherCondition


class WeatherConditionDTO(BaseSchema):
    location_id: UUID
    data_type: WeatherDataType

    def from_dto(
        self,
        weather_from_client: WeatherClientWeatherCurrentConditionSchema | WeatherClientWeatherForecastConditionSchema,
    ) -> WeatherCondition:
        if isinstance(weather_from_client, WeatherClientWeatherCurrentConditionSchema):
            return WeatherCondition(
                location_id=self.location_id,
                data_type=self.data_type,
                date_time=weather_from_client.local_observation_date_time,
                weather_text=weather_from_client.weather_text,
                has_precipitation=weather_from_client.has_precipitation,
                precipitation_type=(
                    PrecipitationType(weather_from_client.precipitation_type)
                    if weather_from_client.precipitation_type
                    else None
                ),
                precipitation_intensity=(
                    PrecipitationIntensity(weather_from_client.precipitation_intensity)
                    if weather_from_client.precipitation_intensity
                    else None
                ),
                temperature_value=weather_from_client.temperature.metric.value,
                temperature_unit=TemperatureUnit(weather_from_client.temperature.metric.unit),
                real_feel_temperature_value=weather_from_client.real_feel_temperature.metric.value,
                real_feel_temperature_unit=TemperatureUnit(weather_from_client.real_feel_temperature.metric.unit),
                wind_speed_value=weather_from_client.wind.speed.metric.value,
                wind_speed_unit=WindSpeedUnit(weather_from_client.wind.speed.metric.unit),
                wind_direction_degrees=weather_from_client.wind.direction.degrees,
                wind_direction_name=WindDirection(weather_from_client.wind.direction.english),
                relative_humidity=weather_from_client.relative_humidity,
                u_v_index=weather_from_client.u_v_index,
                u_v_index_text=weather_from_client.u_v_index_text,
                rain_probability=None,
                snow_probability=None,
                ice_probability=None,
                rain_value=None,
                rain_unit=None,
                snow_value=None,
                snow_unit=None,
                ice_value=None,
                ice_unit=None,
                cloud_cover=weather_from_client.cloud_cover,
                solar_irradiance_value=None,
                solar_irradiance_unit=None,
            )
        return WeatherCondition(
            location_id=self.location_id,
            data_type=self.data_type,
            date_time=weather_from_client.date_time,
            weather_text=weather_from_client.icon_phrase,
            has_precipitation=weather_from_client.has_precipitation,
            precipitation_type=None,
            precipitation_intensity=None,
            temperature_value=weather_from_client.temperature.value,
            temperature_unit=TemperatureUnit(weather_from_client.temperature.unit),
            real_feel_temperature_value=weather_from_client.real_feel_temperature.value,
            real_feel_temperature_unit=TemperatureUnit(weather_from_client.real_feel_temperature.unit),
            wind_speed_value=weather_from_client.wind.speed.value,
            wind_speed_unit=WindSpeedUnit(weather_from_client.wind.speed.unit),
            wind_direction_degrees=weather_from_client.wind.direction.degrees,
            wind_direction_name=WindDirection(weather_from_client.wind.direction.english),
            relative_humidity=weather_from_client.relative_humidity,
            u_v_index=weather_from_client.u_v_index,
            u_v_index_text=weather_from_client.u_v_index_text,
            rain_probability=weather_from_client.rain_probability,
            snow_probability=weather_from_client.snow_probability,
            ice_probability=weather_from_client.ice_probability,
            rain_value=weather_from_client.rain.value,
            rain_unit=PrecipitationUnit(weather_from_client.rain.unit),
            snow_value=weather_from_client.snow.value,
            snow_unit=PrecipitationUnit(weather_from_client.snow.unit),
            ice_value=weather_from_client.ice.value,
            ice_unit=PrecipitationUnit(weather_from_client.ice.unit),
            cloud_cover=weather_from_client.cloud_cover,
            solar_irradiance_value=weather_from_client.solar_irradiance.value,
            solar_irradiance_unit=SolarIrradianceUnit(weather_from_client.solar_irradiance.unit),
        )
