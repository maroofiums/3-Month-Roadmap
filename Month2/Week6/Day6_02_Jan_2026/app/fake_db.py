import asyncio
from schemas import TodoItem    

todo = [
    TodoItem(id=1, title="Buy groceries", description="Milk, Bread, Eggs"),
    TodoItem(id=2, title="Read a book", description="Finish reading '1984' by George Orwell"),
    TodoItem(id=3, title="Exercise", description="Go for a 30-minute run"),
    TodoItem(id=4, title="Call mom", description="Check in with mom about her health"),
]

async def get_all_todos() -> list[TodoItem]:
    await asyncio.sleep(1)
    return todo

async def add_todo(item: TodoItem) -> None:
    await asyncio.sleep(1)
    todo.append(item)
    return todo

async def get_todo_by_id(item_id: int) -> TodoItem | None:
    await asyncio.sleep(1)
    for item in todo:
        if item.id == item_id:
            return item
    return None

async def delete_todo_by_id(item_id: int) -> bool:
    await asyncio.sleep(1)
    for index, item in enumerate(todo):
        if item.id == item_id:
            del todo[index]
            return True
    return False

async def update_todo_by_id(item_id: int, new_item: TodoItem) -> bool:
    await asyncio.sleep(1)
    for index, item in enumerate(todo):
        if item.id == item_id:
            todo[index] = new_item
            return True
    return False
