import os
from functools import lru_cache
from pathlib import Path

from loguru import logger
from pydantic import BaseSettings, PostgresDsn, validator


# Global application variables
PROJECT_PATH = Path(__file__).parent.resolve()
ALEMBIC_FOLDER_PATH = PROJECT_PATH / "database/migrations"
ENVIRONMENT = os.environ.get("ENVIRONMENT", "test")
match ENVIRONMENT:
    case "prod":
        ENV_PATH = PROJECT_PATH / "env/prod.env"
    case "dev":
        ENV_PATH = PROJECT_PATH / "env/dev.env"
    case "local":
        ENV_PATH = PROJECT_PATH / "env/local.env"
    case _:
        ENV_PATH = PROJECT_PATH / "env/pytest.env"
logger.critical(f"config ENV: {ENVIRONMENT}")

logger.info(f"Uploading {ENVIRONMENT} environment.")

DB_URL: PostgresDsn = os.environ.get(
    "DB_URL", "postgresql://postgres:postgres@localhost:5432/postgres"
)


class Settings(BaseSettings):
    HOST: str = os.environ.get("APP_HOST", "localhost")
    PORT: int = os.environ.get("APP_PORT", 8000)

    @validator("PORT")
    def convert_to_int(cls, v) -> int:
        if isinstance(v, int):
            return v
        else:
            return isinstance(v, str)

    class Config:
        env_file = ENV_PATH


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
