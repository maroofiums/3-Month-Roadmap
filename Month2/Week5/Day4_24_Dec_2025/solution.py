from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI()

users_db = []

@app.get("/users/")
def get_users():
    return users_db

@app.get("/users/{user_id}")
def get_user(user_id:int):
    for user in users_db:
        if user.id == user_id:
            return user
        
        return {"error": "User not found"}

@app.post("/search/")
def search_users(query:str):
    result = [user for user in users_db if query.lower() in user.name.lower()]
    return result

@app.post("/users/")
def create_user(user: User):
    users_db.append(user)
    return user

@app.put("/users/{user_id}")
def update_user(user_id:int, updated_user:User):
    for i in range(len(users_db)):
        if users_db[i].id == user_id:
            user_id[i] = updated_user
            return updated_user
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    for i in range(len(users_db)):
        if users_db[i].id == user_id:
            deleted_user = users_db.pop(i)
            return deleted_user
    return {"error": "User not found"}
