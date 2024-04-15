import base64

from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Form
import httpx
import json
from source.services.request_json_data import request_json_data

from starlette.responses import JSONResponse

from source.services.ocr_processor import optichalCharacterRecognitionPaddle
from ..schemas.input_data_schema import InputDataSchema

router = APIRouter()

THIRD_MICROSERVICE_URL = "http://localhost:8002"  # Assuming the second microservice is running on this URL
THIRD_MICROSERVICE_URL += "/api/answerGenerator/LLM/v1"


@router.get("/")
async def get_info():
    return {
        "message": "the role of this service is to generates standarized output format from the user's inputs document "}


#forward request to second microservice"Parser
#    Form: Used to declare form fields in requests, for extracting values from form data.
#    UploadFile: Used to represent uploaded files, for handling file uploads in requests.
#   with UploadFile, FastAPI automatically handles the file upload process
#   In FastAPI, when  uploading a file using a form, the file's data is represented as a bytes-like object.
@router.post("/")
async def parse_received_data_to_sentences_boxes(inputData: InputDataSchema):
    data = await request_json_data(inputData)
    async with httpx.AsyncClient() as client:
        try:

            # Forward the data to the second microservice
            response = await client.post(
                THIRD_MICROSERVICE_URL,
                headers={"Content-Type": "application/json"},
                json=data, timeout=100,
            )
            # Get the status code of the response
            status_code = response.status_code
            #print("***",status_code)
            print("***************", response.content)

            response.raise_for_status()
            return response.content
        except httpx.HTTPStatusError as e:
            # Handle HTTP status errors (4xx or 5xx)
            raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error occurred: {e}") from e
        except httpx.TimeoutException as e:
            # Handle timeout errors
            raise HTTPException(status_code=504, detail="Request to third microservice timed out") from e
        except Exception as e:
            # Handle other exceptions
            raise HTTPException(status_code=500, detail=f"Error in the third microservice: {e}") from e

