from pydantic import BaseModel

class InputDataSchema(BaseModel):
    file_name: str
    file_type: str
    file_data: str
    instruction: str


