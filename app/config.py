# app/config.py

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from .paths import ROOT_DIR


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
    )

    secret_key: SecretStr
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


settings = Settings()  # type: ignore[call-arg] # Loaded from .env file