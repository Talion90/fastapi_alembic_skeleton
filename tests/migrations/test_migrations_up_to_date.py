"""
Test can find cases, when you've changed something in migration and forgot
about models for some reason (or vice versa).
"""
from alembic.command import upgrade
from alembic.config import Config
from alembic.runtime.migration import MigrationContext
from alembic.script import ScriptDirectory
from sqlmodel import Session


def test_migrations_up_to_date(alembic_config: Config, session: Session):
    # Run migrations
    upgrade(alembic_config, "head")

    # Get Alembic migration context
    migration_ctx = MigrationContext.configure(session.connection())
    script_dir = ScriptDirectory.from_config(alembic_config)

    # Get the current version of the Alembic migrations
    current_rev = migration_ctx.get_current_revision()

    # Get the head revision (latest available migration)
    head_rev = script_dir.get_current_head()

    # Compare the current and head revisions
    assert current_rev == head_rev, "Migrations are not up to date"
