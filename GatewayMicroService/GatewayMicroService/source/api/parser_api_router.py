from fastapi import APIRouter, Request,HTTPException,UploadFile,File,Form
import httpx
import json

from source.services.request_handler import  json_data

router = APIRouter()

SECOND_MICROSERVICE_URL = "http://localhost:8001"  # Assuming the second microservice is running on this URL
SECOND_MICROSERVICE_URL+="/api/parser/ocr/v1/"
@router.get("/info")
async def get_info():
    return {"message": "The role of this gateway is to call all  depending childs microservices to get answer of user question about the uploaded file."}


#forward request to second microservice"Parser
#    Form: Used to declare form fields in requests, for extracting values from form data.
#    UploadFile: Used to represent uploaded files, for handling file uploads in requests.
#   with UploadFile, FastAPI automatically handles the file upload process
#   In FastAPI, when  uploading a file using a form, the file's data is represented as a bytes-like object.
@router.post("")
async def forward_request_parser(req: Request,file: UploadFile = File(...), instruction: str = Form(...)):
    async with httpx.AsyncClient() as client:
        try:

            # Prepare json response
            data = await json_data(file=file, instruction=instruction)
            # Forward the data to the second microservice
            response = await client.post(
                    SECOND_MICROSERVICE_URL ,
                    headers={"Content-Type": "application/json"},
                    json=data,timeout=300
                )
            # Get the status code of the response
            status_code = response.status_code
            response.raise_for_status()
            from gtts import gTTS

            # Text to be converted to speech
            text = response.content.__str__()

            # Language in which you want to convert
            language = 'en'

            # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
            tts = gTTS(text=text, lang=language, slow=False)

            # Saving the converted audio in a mp3 file named sample.mp3
            tts.save("sample.mp3")

            return response.content
        except Exception as e:
            #detail of error
            print(f"An error of type {type(e).__name__} occurred")
            raise HTTPException(status_code=500, detail=f"Error in the second microservice : {e}") from e

