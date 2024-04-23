from fastapi import FastAPI
from source.api.ocr_parser_router import router as parser_router


app = FastAPI()



@app.get("/")
async def get_root():


    return {"message": "This is Unified Document Parser mircoservice that can be used to extract text and bouding boxes from documents"}

app.include_router(parser_router, prefix="/api/parser/ocr/v1")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, timeout_keep_alive=600)

