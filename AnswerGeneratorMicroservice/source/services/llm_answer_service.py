"""
We will use a deployed API using Colab now for resource restriction and testing purposes until further discussions.

"""

import httpx
from fastapi import FastAPI, HTTPException, APIRouter
from source.schemas.input_data_schema import InputDataSchema


async def getLLMAnswer(context:InputDataSchema):
    answer = "my bot answer"
    json_output={}
    json_output["texts"]=context.texts
    json_output["boxes"] =context.boxes
    json_output["instruction"] =context.instruction
    async with httpx.AsyncClient() as client:
        try:
            print(json_output["boxes"])
            # Forward the data to the second microservice
            response = await client.post(
                    "https://8196-34-125-167-71.ngrok-free.app/post" ,
                    headers={"Content-Type": "application/json"},
                    json=json_output,timeout=500
                )
            # Get the status code of the response
            status_code = response.status_code
            response.raise_for_status()
            return response.content.decode("utf-8")
        except Exception as e:
            #detail of error
            print(f"An error of type {type(e).__name__} occurred")
            raise HTTPException(status_code=500, detail=f"Error in the colab microservice : {e}") from e
    return json_output