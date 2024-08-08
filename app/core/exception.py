class AppBaseException(Exception):
    def __init__(self, message: str, response: dict | None = None) -> None:
        super().__init__(message)
        self.response = response


class ValidationError(AppBaseException):
    pass
