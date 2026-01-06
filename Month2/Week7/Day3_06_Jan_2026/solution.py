from fastapi import FastAPI,Depends
from jose import jwt 
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

ALGORITHM = "HS256"
SECRET_KEY = "your_secret_key_here"
EXPIRE_MINUTES = 30

demo_data = {
    "name": "user1",
    "password": "admin"
}


def create_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

@app.post("/login")
async def login(form_data:dict):
    if form_data.get("username") != demo_data["name"] or form_data.get("password") != demo_data["password"]:
        return {"error": "Invalid Credentials"}
    
    token = create_token({"sub": form_data.get("username")})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected-route")
async def protected_route(token: str = oauth2_scheme):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return {"error": "Invalid token"}
    except jwt.JWTError:
        return {"error": "Invalid token"}
    
    return {"message": f"Hello, {username}. You have accessed a protected route!"}

@app.get("/protected")
def protected_route(user: str = Depends(protected_route)):
    return {"message": f"Hello {user}, you are authenticated"}