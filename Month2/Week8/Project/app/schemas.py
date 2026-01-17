from pydantic import BaseModel
from typing import Optional

class TodoSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
    