from app.core.exception import AppBaseException


class LocationClientBaseException(AppBaseException):
    pass


class LocationClientApiException(LocationClientBaseException):
    pass


class LocationClientBadRequestException(LocationClientBaseException):
    pass


class LocationClientNotFoundException(LocationClientBaseException):
    pass


class LocationClientInvalidApiKeyException(LocationClientBaseException):
    pass


class LocationClientRequestsExceededException(LocationClientBaseException):
    pass
