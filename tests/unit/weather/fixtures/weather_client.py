from datetime import datetime, timezone
from itertools import count

import pytest
from pytest_mock import MockerFixture

from app.weather.client import (
    IWeatherClient,
    WeatherClientWeatherCurrentConditionSchema,
    WeatherClientWeatherForecastConditionSchema,
)

counter = count()


@pytest.fixture
def weather_client(mocker: MockerFixture) -> IWeatherClient:
    return mocker.Mock(spec=IWeatherClient)


@pytest.fixture
def weather_client_weather_current_condition_schema() -> WeatherClientWeatherCurrentConditionSchema:
    return WeatherClientWeatherCurrentConditionSchema(
        **{
            "LocalObservationDateTime": datetime.now(tz=timezone.utc).isoformat(),
            "EpochTime": 1725729120,
            "WeatherText": "Partly cloudy",
            "WeatherIcon": 35,
            "HasPrecipitation": False,
            "PrecipitationType": None,
            "IsDayTime": False,
            "Temperature": {
                "Metric": {"Value": 26.3, "Unit": "C", "UnitType": 17},
                "Imperial": {"Value": 79.0, "Unit": "F", "UnitType": 18},
            },
            "RealFeelTemperature": {
                "Metric": {"Value": 30.4, "Unit": "C", "UnitType": 17, "Phrase": "Very Warm"},
                "Imperial": {"Value": 87.0, "Unit": "F", "UnitType": 18, "Phrase": "Very Warm"},
            },
            "RealFeelTemperatureShade": {
                "Metric": {"Value": 30.4, "Unit": "C", "UnitType": 17, "Phrase": "Very Warm"},
                "Imperial": {"Value": 87.0, "Unit": "F", "UnitType": 18, "Phrase": "Very Warm"},
            },
            "RelativeHumidity": 83,
            "IndoorRelativeHumidity": 83,
            "DewPoint": {
                "Metric": {"Value": 23.2, "Unit": "C", "UnitType": 17},
                "Imperial": {"Value": 74.0, "Unit": "F", "UnitType": 18},
            },
            "Wind": {
                "Direction": {"Degrees": 203, "Localized": "SSW", "English": "SSW"},
                "Speed": {
                    "Metric": {"Value": 5.6, "Unit": "km/h", "UnitType": 7},
                    "Imperial": {"Value": 3.5, "Unit": "mi/h", "UnitType": 9},
                },
            },
            "WindGust": {
                "Speed": {
                    "Metric": {"Value": 8.2, "Unit": "km/h", "UnitType": 7},
                    "Imperial": {"Value": 5.1, "Unit": "mi/h", "UnitType": 9},
                }
            },
            "UVIndex": 0,
            "UVIndexText": "Low",
            "Visibility": {
                "Metric": {"Value": 16.1, "Unit": "km", "UnitType": 6},
                "Imperial": {"Value": 10.0, "Unit": "mi", "UnitType": 2},
            },
            "ObstructionsToVisibility": "",
            "CloudCover": 31,
            "Ceiling": {
                "Metric": {"Value": 12192.0, "Unit": "m", "UnitType": 5},
                "Imperial": {"Value": 40000.0, "Unit": "ft", "UnitType": 0},
            },
            "Pressure": {
                "Metric": {"Value": 1013.5, "Unit": "mb", "UnitType": 14},
                "Imperial": {"Value": 29.93, "Unit": "inHg", "UnitType": 12},
            },
            "PressureTendency": {"LocalizedText": "Steady", "Code": "S"},
            "Past24HourTemperatureDeparture": {
                "Metric": {"Value": 0.4, "Unit": "C", "UnitType": 17},
                "Imperial": {"Value": 1.0, "Unit": "F", "UnitType": 18},
            },
            "ApparentTemperature": {
                "Metric": {"Value": 28.3, "Unit": "C", "UnitType": 17},
                "Imperial": {"Value": 83.0, "Unit": "F", "UnitType": 18},
            },
            "WindChillTemperature": {
                "Metric": {"Value": 26.1, "Unit": "C", "UnitType": 17},
                "Imperial": {"Value": 79.0, "Unit": "F", "UnitType": 18},
            },
            "WetBulbTemperature": {
                "Metric": {"Value": 24.2, "Unit": "C", "UnitType": 17},
                "Imperial": {"Value": 75.0, "Unit": "F", "UnitType": 18},
            },
            "WetBulbGlobeTemperature": {
                "Metric": {"Value": 25.0, "Unit": "C", "UnitType": 17},
                "Imperial": {"Value": 77.0, "Unit": "F", "UnitType": 18},
            },
            "Precip1hr": {
                "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
            },
            "PrecipitationSummary": {
                "Precipitation": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
                "PastHour": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
                "Past3Hours": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
                "Past6Hours": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
                "Past9Hours": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
                "Past12Hours": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
                "Past18Hours": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
                "Past24Hours": {
                    "Metric": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
                    "Imperial": {"Value": 0.0, "Unit": "in", "UnitType": 1},
                },
            },
            "TemperatureSummary": {
                "Past6HourRange": {
                    "Minimum": {
                        "Metric": {"Value": 26.2, "Unit": "C", "UnitType": 17},
                        "Imperial": {"Value": 79.0, "Unit": "F", "UnitType": 18},
                    },
                    "Maximum": {
                        "Metric": {"Value": 28.1, "Unit": "C", "UnitType": 17},
                        "Imperial": {"Value": 83.0, "Unit": "F", "UnitType": 18},
                    },
                },
                "Past12HourRange": {
                    "Minimum": {
                        "Metric": {"Value": 26.2, "Unit": "C", "UnitType": 17},
                        "Imperial": {"Value": 79.0, "Unit": "F", "UnitType": 18},
                    },
                    "Maximum": {
                        "Metric": {"Value": 32.5, "Unit": "C", "UnitType": 17},
                        "Imperial": {"Value": 90.0, "Unit": "F", "UnitType": 18},
                    },
                },
                "Past24HourRange": {
                    "Minimum": {
                        "Metric": {"Value": 25.8, "Unit": "C", "UnitType": 17},
                        "Imperial": {"Value": 78.0, "Unit": "F", "UnitType": 18},
                    },
                    "Maximum": {
                        "Metric": {"Value": 32.6, "Unit": "C", "UnitType": 17},
                        "Imperial": {"Value": 91.0, "Unit": "F", "UnitType": 18},
                    },
                },
            },
            "MobileLink": "http://www.accuweather.com/en/jp/chiyoda/1511980/current-weather/1511980?lang=en-us",
            "Link": "http://www.accuweather.com/en/jp/chiyoda/1511980/current-weather/1511980?lang=en-us",
        }
    )


@pytest.fixture
def weather_client_weather_forecast_condition_schema() -> WeatherClientWeatherForecastConditionSchema:
    return WeatherClientWeatherForecastConditionSchema(
        **{
            "DateTime": datetime.now(tz=timezone.utc).isoformat(),
            "EpochDateTime": 1725735600,
            "WeatherIcon": 35,
            "IconPhrase": "Partly cloudy",
            "HasPrecipitation": False,
            "IsDaylight": False,
            "Temperature": {"Value": 25.2, "Unit": "C", "UnitType": 17},
            "RealFeelTemperature": {"Value": 30.1, "Unit": "C", "UnitType": 17, "Phrase": "Very Warm"},
            "RealFeelTemperatureShade": {"Value": 30.1, "Unit": "C", "UnitType": 17, "Phrase": "Very Warm"},
            "WetBulbTemperature": {"Value": 24.7, "Unit": "C", "UnitType": 17},
            "WetBulbGlobeTemperature": {"Value": 26.5, "Unit": "C", "UnitType": 17},
            "DewPoint": {"Value": 24.4, "Unit": "C", "UnitType": 17},
            "Wind": {
                "Speed": {"Value": 5.6, "Unit": "km/h", "UnitType": 7},
                "Direction": {"Degrees": 170, "Localized": "S", "English": "S"},
            },
            "WindGust": {"Speed": {"Value": 11.1, "Unit": "km/h", "UnitType": 7}},
            "RelativeHumidity": 95,
            "IndoorRelativeHumidity": 95,
            "Visibility": {"Value": 11.3, "Unit": "km", "UnitType": 6},
            "Ceiling": {"Value": 9144.0, "Unit": "m", "UnitType": 5},
            "UVIndex": 0,
            "UVIndexText": "Low",
            "PrecipitationProbability": 0,
            "ThunderstormProbability": 0,
            "RainProbability": 0,
            "SnowProbability": 0,
            "IceProbability": 0,
            "TotalLiquid": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
            "Rain": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
            "Snow": {"Value": 0.0, "Unit": "cm", "UnitType": 4},
            "Ice": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
            "CloudCover": 34,
            "Evapotranspiration": {"Value": 0.0, "Unit": "mm", "UnitType": 3},
            "SolarIrradiance": {"Value": 0.0, "Unit": "W/m²", "UnitType": 33},
            "MobileLink": "http://www.accuweather.com/en/jp/chiyoda/1511980/hourly-weather-forecast/1511980?day=1&hbhhour=4&unit=c&lang=en-us",
            "Link": "http://www.accuweather.com/en/jp/chiyoda/1511980/hourly-weather-forecast/1511980?day=1&hbhhour=4&unit=c&lang=en-us",
        }
    )
