from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "progettoITAI"
    environment: str = "development"

    database_url: str

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()