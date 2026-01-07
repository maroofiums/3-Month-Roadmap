from fastapi import FastAPI,Depends
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

Secret_KEY = "your_secret_key"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30

def create_token(data:dict):
    to_encode = data.copy()
    encode_jwt = jwt.encode(to_encode, Secret_KEY, algorithm=ALGORITHM)
    return encode_jwt

@app.post("/token")
def login(form_data: dict):
    if form_data.get("username") == "user" and form_data.get("password") == "pass":
        token = create_token({"sub": form_data["username"]})
        return {"access_token": token, "token_type": "bearer"}
    return {"error": "Invalid credentials"}

@app.get("/protected-route")
def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, Secret_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return {"error": "Invalid token"}
        return {"message": f"Hello, {username}. You have accessed a protected route!"}
    except jwt.JWTError:
        return {"error": "Invalid token"}
    
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI JWT Authentication Example"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)