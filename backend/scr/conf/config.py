from pydantic_settings import BaseSettings
from pydantic import ConfigDict, EmailStr


class Config(BaseSettings):
    DATA_BASE_URL: str

    SECRET_KEY_JWT: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    MAIL_USERNAME: EmailStr
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str

    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


config = Config()
