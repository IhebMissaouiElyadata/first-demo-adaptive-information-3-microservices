from pydantic import  Field
import os
# To this import statement
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    app_name: str = Field(default=os.getenv("APP_NAME", "myapp"))
    debug: bool = Field(default=False)
    database_url: str = Field(default="sqlite:///app.db")

