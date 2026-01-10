from auth import fake_user, create_access_token
from todo import router as todo_router
from fastapi import FastAPI, HTTPException, Depends
from middleware import logging_middleware

app = FastAPI()
app.middleware("http")(logging_middleware)

@app.post("/login")
def login(username: str, password: str):
    if username == fake_user["username"] and password == fake_user["password"]:
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
app.include_router(todo_router, prefix="/todos", tags=["todos"])
