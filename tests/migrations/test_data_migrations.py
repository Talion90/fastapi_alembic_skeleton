"""
Check data is migrated correctly in "data" migrations.
See data_migrations/migration_*.py for example.
"""
from typing import Callable

import pytest
from alembic.command import downgrade, upgrade

from utils import make_validation_params_groups
from tests.migrations.data_migrations import migration_86e8ca550d04_cars


def get_data_migrations():
    """
    Returns tests for data migrations, from tests/data_migrations folder.
    """
    return make_validation_params_groups(
        migration_86e8ca550d04_cars,
    )


@pytest.mark.parametrize(
    ("rev_base", "rev_head", "on_init", "on_upgrade", "on_downgrade"),
    get_data_migrations(),
)
def test_data_migrations(
    alembic_config,
    engine,
    session,
    rev_base: str,
    rev_head: str,
    on_init: Callable,
    on_upgrade: Callable,
    on_downgrade: Callable,
):
    # Upgrade to previous migration before target and add some data,
    # that would be changed by tested migration.
    upgrade(alembic_config, rev_base)
    on_init(engine=engine, session=session)

    # Perform upgrade in tested migration.
    # Check that data is migrated correctly in on_upgrade callback
    upgrade(alembic_config, rev_head)
    on_upgrade(session=session)

    # Perform downgrade in tested migration.
    # Check that changes are reverted back using on_downgrade callback
    downgrade(alembic_config, rev_base)
    on_downgrade(session=session)
