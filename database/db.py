from collections.abc import Generator

from sqlmodel import Session, create_engine

from config import DB_URL


def get_session() -> Generator[Session, None, None]:
    """SQLModel Session generator"""
    engine = create_engine(DB_URL)
    with Session(engine) as session:
        yield session
