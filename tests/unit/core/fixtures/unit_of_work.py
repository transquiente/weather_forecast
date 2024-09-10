import pytest
from pytest_mock import MockerFixture

from app.core.repository import UnitOfWork


@pytest.fixture
def unit_of_work(mocker: MockerFixture) -> UnitOfWork:
    unit_of_work = mocker.AsyncMock(spec=UnitOfWork)
    unit_of_work.commit.return_value = None
    unit_of_work.rollback.return_value = None
    unit_of_work.flush.return_value = None
    unit_of_work.expire_all.return_value = None
    unit_of_work.expunge.return_value = None
    unit_of_work.expunge_all.return_value = None
    return unit_of_work
