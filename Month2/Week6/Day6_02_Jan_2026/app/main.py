from fake_db import *
from schemas import TodoItem
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

@app.get("/todos", response_model=List[TodoItem])
async def read_todos():
    return await get_all_todos()

@app.post("/todos", response_model=List[TodoItem])
async def create_todo(item: TodoItem):
    return await add_todo(item)

@app.get("/todos/{item_id}", response_model=TodoItem)
async def read_todo(item_id: int):
    item = await get_todo_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return item

@app.delete("/todos/{item_id}", response_model=dict)
async def delete_todo(item_id: int):
    success = await delete_todo_by_id(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"detail": "Todo item deleted"}

@app.put("/todos/{item_id}", response_model=dict)
async def update_todo(item_id: int, new_item: TodoItem):
    success = await update_todo_by_id(item_id, new_item)
    if not success:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"detail": "Todo item updated"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

