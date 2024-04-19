
import base64
from fastapi import UploadFile

"""
This is a method to the Uploaded image to  base 64 string encoded data and make json output 


"""
async def InputDataToJson(file: UploadFile = None, instruction: str = None):
    # Prepare the data to be forwarded
    data = {}

    # Handle file uploads
    if file is not None:
        data["file_name"] = file.filename
        data["file_type"] = file.content_type
        data["file_data"] = base64.b64encode( await file.read()).decode("utf-8")

    if instruction is not None:
        data["instruction"] = instruction
    return data

