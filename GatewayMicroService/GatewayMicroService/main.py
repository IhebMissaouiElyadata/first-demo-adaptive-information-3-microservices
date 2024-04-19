from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse

from config.settings import AppConfig
from source.api.router import router as parser_router

app_config = AppConfig()
app = FastAPI(debug=True)



@app.get("/")
async def get_root():


    return {"message": "This is a gateway to the Document LLM backend services."}

app.include_router(parser_router, prefix="/gateway")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, timeout_keep_alive=280)
