from pydantic import BaseModel
from typing import Any


class GlobalResponse(BaseModel):
    status: str = "success"
    message: str = ""
    data: Any = None
    pagination: dict = {}