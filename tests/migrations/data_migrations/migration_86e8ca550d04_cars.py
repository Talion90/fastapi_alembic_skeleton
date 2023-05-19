"""
Data migration test example.

MUST-have properties:
  - rev_base
    Previous migration identifier
  - rev_head
    Current (being tested) migration identifier

Optional properties:
  - on_init(engine)
    Is called before applying 'rev_head' migration. Can be used to add some
    data before migration is applied.
  - on_upgrade(engine)
    Is called after applying 'rev_head' migration. Can be used to check data
    was migrated successfully by upgrade() migration method.
  - on_downgrade(engine)
    Is called after migration is rolled back to 'rev_base'. Can be used to
    check data was rolled back to initial state.
"""
from sqlalchemy.engine import Engine
from sqlmodel import Session, select, SQLModel

# Load migration as module
from database.models import Company
from utils import load_migration_as_module


migration = load_migration_as_module("86e8ca550d04_cars.py")
rev_base: str = migration.down_revision
rev_head: str = migration.revision

# We can reuse objects from migration.
# Pytest call each test in separate process, so you could use global variables
# for this test to store state.
companies = [
    Company(name="BMW"),
    Company(name="Porsche"),
]


def on_init(engine: Engine, session: Session):
    """
    Create rows in companies table before migration is applied
    """
    SQLModel.metadata.create_all(engine)


def on_upgrade(session: Session):
    """
    Ensure that data was successfully migrated
    """
    global companies

    stmt = select(Company)
    actual = session.exec(stmt).all()

    assert len(actual) == 2


def on_downgrade(session: Session):
    """
    Ensure that data changes were rolled back
    """
    global companies

    stmt = select(Company)
    actual = session.exec(stmt).all()
    assert actual == []
