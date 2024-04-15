from pydantic_settings import BaseSettings
import os


class Appconfig(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    debug: bool = False
    database_url: str = "postgresql://"+os.getenv("DB_USER")+":"+os.getenv("DB_PASSWORD")+"@"+os.getenv("DB_HOST")+"/"+os.getenv("DB_NAME")

