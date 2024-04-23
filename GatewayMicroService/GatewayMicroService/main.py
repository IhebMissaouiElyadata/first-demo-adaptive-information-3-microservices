from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from config.settings import  get_app_config
from config.settings import AppConfig
from source.api.router import router as parser_router

app = FastAPI(debug=True)
# Dependency provider function to provide the app_config instance

@app.get("/")
async def get_root():


    return {"message": "This is a gateway to the Document LLM backend services."}

app.include_router(parser_router, prefix="/gateway")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, timeout_keep_alive=280)
