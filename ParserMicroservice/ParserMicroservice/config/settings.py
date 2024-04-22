from pydantic_settings import BaseSettings
import os


class Appconfig(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    debug: bool = False

