from fastapi import APIRouter, Request
import httpx
router = APIRouter()



@router.get("/{info}")
async def get_user(user_id:str):
    return {"message": "the role of this service is to login user "}

@router.get("/forward")
async def forward_request_parser(request: Request):
    url = "http://microservice-url:8000"  # Replace with the URL of your microservice
    async with httpx.AsyncClient() as client:
        response = await client.get(url + request.url.path)
    return response.json()
