from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user

router = APIRouter()

todo_list = []

@router.get("/todos/")
async def read_todos(current_user: str = Depends(get_current_user)):
    return {"todos": todo_list, "user": current_user}

@router.post("/todos/")
async def create_todo(item: str, current_user: str = Depends(get_current_user)):
    todo_list.append(item)
    return {"message": "Todo item added", "item": item, "user": current_user}

@router.delete("/todos/{item_id}")
async def delete_todo(item_id: int, current_user: str = Depends(get_current_user)):
    if item_id < 0 or item_id >= len(todo_list):
        raise HTTPException(status_code=404, detail="Item not found")
    removed_item = todo_list.pop(item_id)
    return {"message": "Todo item deleted", "item": removed_item, "user": current_user}

@router.put("/todos/{item_id}")
async def update_todo(item_id: int, new_item: str, current_user: str = Depends(get_current_user)):
    if item_id < 0 or item_id >= len(todo_list):
        raise HTTPException(status_code=404, detail="Item not found")
    todo_list[item_id] = new_item
    return {"message": "Todo item updated", "item": new_item, "user": current_user}
