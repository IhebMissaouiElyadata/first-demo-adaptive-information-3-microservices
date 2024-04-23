from pydantic import  Field
import os
# To this import statement
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    app_name: str = Field(default=os.getenv("APP_NAME", "answer generator microservice"))
    debug: bool = Field(default=False)
    COLAB_MICROSERVICE_URL:str=Field(default=os.getenv("answer_gen_APP","https://3aca-35-247-170-134.ngrok-free.app/post"))
# Instantiate the configuration
app_config = AppConfig()

# Dependency provider function to provide the app_config instance
def get_app_config():

    return app_config
