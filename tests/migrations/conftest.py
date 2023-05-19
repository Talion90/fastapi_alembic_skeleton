import pytest
from sqlalchemy import create_engine
from sqlmodel import Session
from yarl import URL

from utils import alembic_config_from_url, tmp_database


@pytest.fixture
def postgres(pg_url: URL):
    """
    Creates empty temporary database.
    """
    with tmp_database(pg_url, "pytest") as tmp_url:
        yield tmp_url


@pytest.fixture()
def engine(postgres):
    """
    SQLModel engine, bound to temporary database.
    """
    engine = create_engine(postgres, echo=True)
    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture()
def session(engine):
    """
    SQLModel Session, bound to temporary database.
    """
    with Session(engine) as session:
        yield session


@pytest.fixture()
def alembic_config(postgres):
    """
    Alembic configuration object, bound to temporary database.
    """
    return alembic_config_from_url(postgres)
