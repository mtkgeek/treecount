import logging
import os
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    debug: bool = os.getenv("DEBUG", True)
    secret: str = os.getenv(
        "SECRET", "66b8b781bf1330ea0c8b6558c66e5536870933859c637571")
    # use_ngrok: str = os.getenv(
    #     "USE_NGROK", True)

    database_url: str = os.getenv(
        "DATABASE_URL", "sqlite:///database.db")

    imagekit_private_key: str = os.getenv(
        "IMAGEKIT_PRIVATE_KEY", "sqlite:///database.db")

    imagekit_public_key: str = os.getenv(
        "IMAGEKIT_PUBLIC_KEY", "sqlite:///database.db")

    imagekit_url_endpoint: str = os.getenv(
        "IMAGEKIT_URL_ENDPOINT", "testnetrh5lAFGlMX8bYTwXsVbbdv3s5IKMrmUb")

    mail_username: str = os.getenv(
        "MAIL_USERNAME", "dsfcghvj")
    mail_password: str = os.getenv(
        "MAIL_PASSWORD", "dxfgc")
    mail_to: str = os.getenv("MAIL_TO", "support@blank.com")
    mail_from: str = os.getenv("MAIL_FROM", "blank@mail.com")
    mail_port: int = os.getenv("MAIL_PORT", 45)
    mail_server: str = os.getenv("MAIL_SERVER", "bghj")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
