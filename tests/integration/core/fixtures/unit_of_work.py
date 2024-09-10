import pytest
from sqlalchemy.orm import Session

from app.core.repository.sql import UnitOfWork


@pytest.fixture
def unit_of_work(db_session: Session) -> UnitOfWork:
    return UnitOfWork(db_session)
