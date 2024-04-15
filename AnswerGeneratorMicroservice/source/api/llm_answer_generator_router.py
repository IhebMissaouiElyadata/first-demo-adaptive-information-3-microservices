from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from ..schemas.input_data_schema import InputDataSchema
import logging

from ..services.llm_answer_service import getLLMAnswer

router = APIRouter()
logger = logging.getLogger(__name__)
@router.get("/")
async def get_info():
    return {
        "message": "The role of this service is to generate a user's answer based on LLM."
    }

@router.post("")
async def get_context_answer_from_llm(context_OCR_OUTPUT_FOR_NOW: InputDataSchema):
    try:
        # logger.debug("Debug message")
        # logger.info("Info message")
        # logger.warning("Warning message")
        # logger.error("Error message")
        # logger.critical("Critical message")
        # Process the incoming data here
        answer=await getLLMAnswer(context_OCR_OUTPUT_FOR_NOW)

        # For now, let's just return a success message
        return answer
    except Exception as e:
        # If an error occurs during processing, raise an HTTP 500 error with the error message
        raise HTTPException(status_code=500, detail=f"Error processing data: {e}")
