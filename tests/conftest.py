import os

import pytest
from dotenv import load_dotenv
from yarl import URL


@pytest.fixture(autouse=True)
def load_env_variables():
    # Automatically load environment variables before each test
    load_dotenv("env/pytest.env")


@pytest.fixture(scope="session")
def pg_url():
    """
    Provides base PostgreSQL URL for creating temporary databases.
    """
    load_dotenv("env/pytest.env")
    os.environ["ENVIRONMENT"] = "test"
    print("ENVIROMMENT ",os.environ["ENVIRONMENT"])
    from config import DB_URL
    return URL(DB_URL)
