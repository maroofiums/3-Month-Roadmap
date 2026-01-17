from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import LocalSession
from models import Todo
from schemas import TodoSchema
from auth import get_current_user, create_token

router = APIRouter(prefix="/todos", tags=["todos"])

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TodoSchema])
def get_all_todos(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """Get all todos - requires authentication"""
    todos = db.query(Todo).all()
    return todos

@router.get("/{todo_id}", response_model=TodoSchema)
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """Get a specific todo by ID - requires authentication"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", response_model=TodoSchema)
def create_todo(todo: TodoSchema, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """Create a new todo - requires authentication"""
    db_todo = Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.put("/{todo_id}", response_model=TodoSchema)
def update_todo(todo_id: int, todo: TodoSchema, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """Update a todo - requires authentication"""
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """Delete a todo - requires authentication"""
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}