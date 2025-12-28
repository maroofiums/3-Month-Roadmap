from fastapi import APIRouter
from Week5.Day7_27_Dec_2025.app.schemas import Todo

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

todo_db = []

@router.post("/")
def create_todo(todo: Todo):
    todo_db.append(todo)
    return todo

@router.get("/")
def get_todos():
    return todo_db

@router.get("/{todo_id}")
def get_todo(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}

@router.put("/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            todo_db[index] = updated_todo
            return updated_todo
    return {"error": "Todo not found"}


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            del todo_db[index]
            return {"message": "Todo deleted"}
    return {"error": "Todo not found"}

@router.get("/search/")
def search_todos(query: str):
    results = [todo for todo in todo_db if query.lower() in todo.title.lower()]
    return results
