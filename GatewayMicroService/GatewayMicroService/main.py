from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from source.api.parser_api_router import router as parser_router
from source.api.login_api import router as login_router


app = FastAPI(debug=True)



@app.get("/")
async def get_root():


    return {"message": "This is a gateway to the Document LLM backend services."}

app.include_router(parser_router, prefix="/gateway")
# not created yet
app.include_router(login_router, prefix="/login_api")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, timeout_keep_alive=280)
