import logging

import httpx
from fastapi import HTTPException, Depends

from config.settings import AppConfig, get_app_config
from source.schemas.input_data_schema import InputDataSchema
import config.settings

async def getLLMAnswer(context:InputDataSchema,appConfig: AppConfig ):
    """
    We will use a deployed API using Colab now for resource restriction and testing purposes until further discussions.

    """

    json_data={}
    json_data["texts"]=context.texts
    json_data["boxes"] =context.boxes
    json_data["instruction"] =context.instruction
    async with httpx.AsyncClient() as client:

            # Forward the data to the second microservice
            response = await client.post(
                    appConfig.COLAB_MICROSERVICE_URL ,
                    headers={"Content-Type": "application/json"},
                    json=json_data,timeout=500
                )
            # Get the status code of the response
            status_code = response.status_code
            if status_code !=  200:
                logging.log(level=logging.ERROR, msg=f"Colab API returned {status_code}")


                raise HTTPException(status_code=500, detail=f"An error  in the colab microservice : ")

            answer=response.content.decode("utf-8")
            return answer

