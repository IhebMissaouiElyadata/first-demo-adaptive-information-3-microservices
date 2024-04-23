from pydantic import  Field
import os
# To this import statement
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    app_name: str = Field(default=os.getenv("APP_NAME", "parsing micro service"))
    debug: bool = Field(default=False)
    THIRD_MICROSERVICE_URL:str=Field(default=os.getenv("ANS_GEN_ENDPOINT","http://localhost:8004/api/answerGenerator/LLM/v1"))
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
