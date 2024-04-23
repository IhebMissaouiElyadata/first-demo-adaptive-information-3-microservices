from pydantic import  Field
import os
# To this import statement
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    app_name: str = Field(default=os.getenv("APP_NAME", "gateway microservice"))
    debug: bool = Field(default=False)
    SECOND_MICROSERVICE_URL:str=Field(default=os.getenv("PARSER_ENDPOINT","http://localhost:8001/api/parser/ocr/v1/"))
# Instantiate the configuration
app_config = AppConfig()

# Dependency provider function to provide the app_config instance
def get_app_config():

    return app_config
import logging
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)
