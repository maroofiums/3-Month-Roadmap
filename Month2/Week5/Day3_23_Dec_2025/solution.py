from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = []

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/")
def create_user(user: User):
    user_db.append(user)
    return {"message": "User created successfully", "user": user}

@app.get("/users/")
def get_users():
    return {"users": user_db}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in user_db:
        if user.id == user_id:
            return {"user": user}
    return {"message": "User not found"}, 404

# path and query parameters example

@app.get("/search/")
def search_users(name: str):
    result = [user for user in user_db if name.lower() in user.name.lower()]
    return {"users": result}

@app.get("/users/{user_id}/details/")
def get_user_details(user_id: int, include_email: bool = False):
    for user in user_db:
        if user.id == user_id:
            if include_email:
                return {"user": user}
            else:
                return {"user": {"id": user.id, "name": user.name}}
    return {"message": "User not found"}, 404

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)