from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Config(BaseSettings):
    DATA_BASE_URL: str

    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


config = Config()
