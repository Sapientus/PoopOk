from pydantic_settings import BaseSettings
from pydantic import ConfigDict, EmailStr


class Config(BaseSettings):
    """Database"""
    DATA_BASE_URL: str

    """JWT Token"""
    SECRET_KEY_JWT: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    """Mail Transfer"""
    MAIL_USERNAME: EmailStr
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str

    """Cloud Service"""
    CLOUD_NAME: str
    API_KEY: str
    API_SECRET: str

    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


config = Config()
