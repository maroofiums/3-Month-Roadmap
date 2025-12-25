from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr

class User(BaseModel):
    id : int
    name: str
    email: EmailStr 


app= FastAPI()

users_db = []

@app.post("/users/")
def create_user(user:User):
    for u in users_db:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(user)
    return user

@app.get("/users/")
def get_users():
    return users_db

@app.get("/user/{user_id}")
def get_user(user_id:int):
    for u in users_db:
        if u.id == user_id:
            return u
        raise HTTPException(status_code=404, detail="User not found")
    

@app.get("/search/")
def search_user(query:str):
    result = [user for user in users_db if query.lower() in user.name.lower() or query.lower() in user.email.lower() ]
    return result

@app.get("/user/{user_id}")
def get_user(user_id:int,updated_user:User):
    for i in range(len(users_db)):
        if users_db[i].id == user_id:
            users_db[i] = updated_user
            return users_db[i]
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
def delete_user(user_id:int):
    for i in range(len(users_db)):
        if users_db[i].id == user_id:
            deleted_user = users_db.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")


