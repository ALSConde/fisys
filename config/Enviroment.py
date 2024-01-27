import os
from functools import lru_cache
from pydantic import BaseSettings


@lru_cache
def get_settings():
    runtime_env = os.getenv("DEV", "ENV")
    return f"env.{runtime_env}" if runtime_env == "DEV" else f"env.prod"

class Settings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str
    DATABASE_USERNAME: str
    DEBUG_MODE: bool

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_TIME_MINUTES: int

    class Config:
        env_file = get_settings()
        env_file_encoding = "utf-8"

@lru_cache
def get_env():
    return Settings()
    