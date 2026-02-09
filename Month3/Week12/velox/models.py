from sqlmodel import SQLModel, Field

class VeloxBase(SQLModel):
    id: int = Field(default=None, primary_key=True)
