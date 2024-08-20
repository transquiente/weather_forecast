from enum import Enum


class WeatherDataType(Enum):
    CURRENT_CONDITION = "current_condition"
    FORECAST_CONDITION = "forecast_condition"


class PrecipitationType(str, Enum):
    RAIN = "rain"
    SNOW = "snow"
    ICE = "ice"
    MIXED = "mixed"


class PrecipitationIntensity(str, Enum):
    LIGHT = "light"
    MODERATE = "moderate"
    HEAVY = "heavy"


class TemperatureUnit(str, Enum):
    CELSIUS = "C"
    FAHRENHEIT = "F"
    KELVIN = "K"


class WindSpeedUnit(str, Enum):
    KILOMETERS_PER_HOUR = "km/h"
    MILES_PER_HOUR = "mph"
    METERS_PER_SECOND = "m/s"
    KNOTS = "kn"


class WindDirection(str, Enum):
    NORTH = "N"
    NORTH_NORTHEAST = "NNE"
    NORTHEAST = "NE"
    EAST_NORTHEAST = "ENE"
    EAST = "E"
    EAST_SOUTHEAST = "ESE"
    SOUTHEAST = "SE"
    SOUTH_SOUTHEAST = "SSE"
    SOUTH = "S"
    SOUTH_SOUTHWEST = "SSW"
    SOUTHWEST = "SW"
    WEST_SOUTHWEST = "WSW"
    WEST = "W"
    WEST_NORHTWEST = "WNW"
    NORTHWEST = "NW"
    NORTH_NORTHWEST = "NNW"


class PrecipitationUnit(str, Enum):
    CM = "cm"
    MM = "mm"


class SolarIrradianceUnit(str, Enum):
    WATT_PER_SQUARE_METRE = "W/m²"
