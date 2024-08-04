from pydantic import AnyUrl
from pydantic_settings import BaseSettings
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

DEFAULT_DB_SCHEME = "postgresql+psycopg2"


class DBSettings(BaseSettings):
    scheme: str = DEFAULT_DB_SCHEME
    username: str
    password: str
    host: str
    port: int
    database: str
    pool_size: int = 15
    max_overflow: int = 10

    class Config:
        env_prefix = "db_"

    @property
    def dsn(self) -> str:
        return str(
            AnyUrl.build(
                scheme=self.scheme,
                username=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                path=self.database,
            )
        )


def get_settings() -> DBSettings:
    return DBSettings()


def get_engine() -> Engine:
    db_settings = get_settings()
    return create_engine(
        db_settings.dsn,
        pool_pre_ping=True,
        pool_size=db_settings.pool_size,
        max_overflow=db_settings.max_overflow,
        pool_recycle=3600,
    )


def session_maker_factory() -> sessionmaker:
    engine = get_engine()
    return sessionmaker(bind=engine, expire_on_commit=False)


class UnitOfWork:
    def __init__(self, session: Session) -> None:
        self.session = session

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        self.session.expunge_all()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def flush(self) -> None:
        self.session.flush()

    def expire_all(self) -> None:
        self.session.expire_all()

    def expunge(self, instance) -> None:
        self.session.expunge(instance)

    def expunge_all(self) -> None:
        self.session.expunge_all()
