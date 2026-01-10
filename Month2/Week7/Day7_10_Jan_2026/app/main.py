from auth import fake_user, create_access_token
from todo import router as todo_router
from fastapi import FastAPI, HTTPException, Depends
from middleware import logging_middleware
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()
app.middleware("http")(logging_middleware)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if username != fake_user["username"] or password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}