from pydantic import BaseModel

class TitanicInput(BaseModel):
    pclass: int
    sex: int
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked_Q: int
    embarked_S: int

class TitanicOutput(BaseModel):
    survived: int
