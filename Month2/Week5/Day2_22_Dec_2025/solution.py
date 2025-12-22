from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    
users_db = []
app = FastAPI()
@app.post("/users/")
def create_user(user: User):
    if any(u.id == user.id for u in users_db):
        return {"error": "User with this ID already exists."}
    users_db.append(user)
    return user
