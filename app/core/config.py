import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    github_pat: str
    github_api_base: str = "https://api.github.com"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
