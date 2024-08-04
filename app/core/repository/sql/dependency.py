from collections.abc import Iterator

from fastapi import Depends, Request
from sqlalchemy.orm import Session, sessionmaker

from app.core.repository.sql import UnitOfWork


def get_session(request: Request) -> Iterator[Session]:
    session_maker: sessionmaker = request.app.state.session_maker
    with session_maker() as session:
        yield session


def get_uow(session: Session = Depends(get_session)) -> UnitOfWork:
    return UnitOfWork(session)
