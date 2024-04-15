from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.responses import JSONResponse

from source.schemas.input_data_schema import InputDataSchema
from source.services.llm_answer_service import getLLMAnswer
from source.api.llm_answer_generator_router import router as answergeneratorLLMRouter
app = FastAPI(debug=True)
@app.get("/")
async def get_root():
    return {"message": "This is answer generator microservice"}

app.include_router(answergeneratorLLMRouter, prefix="/api/answerGenerator/LLM/v1")
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )
