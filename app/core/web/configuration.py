from typing import TypeVar

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError as PydanticValidationError
from starlette.middleware.cors import CORSMiddleware

from app.core.exception import AppBaseException
from app.core.repository import ObjectAlreadyExists, ObjectNotFound
from app.core.web.settings import get_cors_settings

ExceptionType = TypeVar("ExceptionType", bound=type[Exception])
PydanticValidationErrorType = TypeVar("PydanticValidationErrorType", bound=type[PydanticValidationError])


def configure_cors(app: FastAPI) -> None:
    cors_settings = get_cors_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_settings.allow_origins,
        allow_methods=cors_settings.allow_methods,
        allow_headers=cors_settings.allow_headers,
        allow_credentials=cors_settings.allow_credentials,
    )


def add_exception_handler(
    app: FastAPI,
    exception_type: ExceptionType,
    status_code: int,
) -> None:
    def handler(request: Request, exception: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={"message": str(exception)},
        )

    app.add_exception_handler(exception_type, handler)  # type: ignore


def add_pydantic_validation_error_exception_handler(
    app: FastAPI,
    exception_type: PydanticValidationErrorType,
    status_code: int,
) -> None:
    def handler(request: Request, exception: PydanticValidationError) -> JSONResponse:
        errors = exception.errors()
        for error in errors:
            error.pop("input", None)
        return JSONResponse(
            status_code=status_code,
            content={"detail": errors},
        )

    app.add_exception_handler(exception_type, handler)  # type: ignore


def configure_error_handlers(app: FastAPI) -> None:
    add_exception_handler(app, AppBaseException, status.HTTP_400_BAD_REQUEST)
    add_pydantic_validation_error_exception_handler(app, PydanticValidationError, status.HTTP_400_BAD_REQUEST)
    add_exception_handler(app, ObjectNotFound, status.HTTP_404_NOT_FOUND)
    add_exception_handler(app, ObjectAlreadyExists, status.HTTP_409_CONFLICT)
