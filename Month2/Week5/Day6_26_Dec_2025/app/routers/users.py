from fastapi import APIRouter, HTTPException
from app.schemas import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

users_db = []

@router.get("/")
async def get_users():
    return users_db

@router.get("/{user_id}")
async def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/")
async def create_user(user: User):
    users_db.append(user)
    return user

@router.put("/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            del users_db[index]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/search/")
async def search_users(name: str):
    result = [user for user in users_db if name.lower() in user.name.lower()]
    return result