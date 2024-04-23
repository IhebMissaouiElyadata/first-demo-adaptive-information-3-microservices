from fastapi import APIRouter, Depends

from config.settings import AppConfig, get_app_config
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
async def get_context_answer_from_llm(context_OCR_OUTPUT_FOR_NOW: InputDataSchema,appConfig: AppConfig = Depends(get_app_config)  ):
        print("im here")
        answer=await getLLMAnswer(context_OCR_OUTPUT_FOR_NOW,appConfig)

        return answer

