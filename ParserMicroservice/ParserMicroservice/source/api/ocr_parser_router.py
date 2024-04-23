
from fastapi import APIRouter,  Depends
import httpx
from config.settings import  get_app_config
from config.settings import AppConfig
from source.services.request_json_data import request_json_data

from ..schemas.input_data_schema import InputDataSchema

router = APIRouter()



@router.get("/")
async def get_info():
    return {
        "message": "the role of this service is to generates standarized output format from the user's inputs document "}



@router.post("/")
async def parse_received_data_to_sentences_boxes(inputData: InputDataSchema,appConfig: AppConfig = Depends(get_app_config)):
    data = await request_json_data(inputData)

    async with httpx.AsyncClient() as client:
            print (appConfig.THIRD_MICROSERVICE_URL)

            # Forward the data to the second microservice
            response = await client.post(
                appConfig.THIRD_MICROSERVICE_URL,
                headers={"Content-Type": "application/json"},
                json=data, timeout=100,
            )
            #print("***",status_code)
            if (response.status_code !=200):
                raise Exception("HTTP Exception from Answer generation microservice ")
            return response.content

