from fastapi import FastAPI

from source.api.llm_answer_generator_router import router as answergeneratorLLMRouter
app = FastAPI(debug=True)
@app.get("/")
async def get_root():
    return {"message": "This is answer generator microservice"}

app.include_router(answergeneratorLLMRouter, prefix="/api/answerGenerator/LLM/v1")
