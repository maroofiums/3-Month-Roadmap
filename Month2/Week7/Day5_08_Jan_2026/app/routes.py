from fastapi import APIRouter,Depends
from auth import get_current_user

router = APIRouter()

@router.get("/protected-route")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}. You have accessed a protected route!"}
@router.get("/public-route")
async def public_route():
    return {"message": "Hello, this is a public route accessible to everyone!"}
