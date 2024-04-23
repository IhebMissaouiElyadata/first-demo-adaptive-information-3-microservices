from fastapi import APIRouter,UploadFile,File,Form,Depends
import httpx
import  logging
from config.settings import AppConfig
from main import get_app_config
from source.services.data_to_json import  InputDataToJson
router = APIRouter()
# Assuming the second microservice is running on this URL
@router.get("/info")
async def get_info():
    return {"message": "The role of this gateway is to call all  depending childs microservices to get answer of user question about the uploaded file."}


#forward request to second microservice "Parser"
@router.post("")
async def forward_request_to_parser(file: UploadFile = File(...), instruction: str = Form(...),appConfig:AppConfig = Depends(get_app_config)):
    async with httpx.AsyncClient() as client:
            logging.info(f"Parsing URL ...{appConfig.SECOND_MICROSERVICE_URL}")
            # Prepare json response
            data = await InputDataToJson(file=file, instruction=instruction)
            print( appConfig.SECOND_MICROSERVICE_URL)
            # Forward the data to the second microservice
            response = await client.post(
                    appConfig.SECOND_MICROSERVICE_URL ,
                    headers={"Content-Type": "application/json"},
                    json=data,timeout=500
                )
            # Get the status code of the response
            status_code = response.status_code


            if (status_code != 200):
                raise Exception(f"HTTP Exception from Parsing  microservice {status_code} ")
            return response.content



