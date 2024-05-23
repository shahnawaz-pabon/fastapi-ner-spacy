from pydantic import BaseModel

class InputTextBody(BaseModel):
    input_text: str