from pydantic import BaseModel

class InputDataSchema(BaseModel):
    texts: list
    boxes: list
    scores: list
    instruction:str

