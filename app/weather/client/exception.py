from app.core.exception import AppBaseException


class WeatherClientBaseException(AppBaseException):
    pass


class WeatherClientApiException(WeatherClientBaseException):
    pass


class WeatherClientBadRequestException(WeatherClientBaseException):
    pass


class WeatherClientNotFoundException(WeatherClientBaseException):
    pass


class WeatherClientInvalidApiKeyException(WeatherClientBaseException):
    pass


class WeatherClientRequestsExceededException(WeatherClientBaseException):
    pass
