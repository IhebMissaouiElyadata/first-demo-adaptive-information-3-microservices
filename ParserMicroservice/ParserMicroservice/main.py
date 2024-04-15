from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from source.api.ocr_parser_router import router as parser_router


app = FastAPI()



@app.get("/")
async def get_root():


    return {"message": "This is Unified Document Parser mircoservice that can be used to extract text and bouding boxes from documents"}

app.include_router(parser_router, prefix="/api/parser/ocr/v1")
# another appraoch for LLAVA USAGE
#app.include_router(login_router, prefix="/")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )
