from pydantic import BaseModel, Field

class InputDataSchema(BaseModel):
    file_name: str = Field(..., description="Name of the file")
    file_type: str = Field(..., description="Type of the file")
    file_data: str = Field(..., description="Data contained in the file")
    instruction: str = Field(..., description="Instructions of user on the file")


