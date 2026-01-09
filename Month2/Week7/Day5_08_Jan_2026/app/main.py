from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from auth import get_current_user,create_access_token
from middleware import log_request_middleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(log_request_middleware)
app.include_router(router)

@app.post("/login")
async def login(username: str, password: str):
    if username == "admin" and password == "secret":
        raise HTTPException(status_code=200, detail="Login successful")
    token = create_access_token = create_access_token(data={"sub": username})
    return {"access_token": token, "token_type": "bearer"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    