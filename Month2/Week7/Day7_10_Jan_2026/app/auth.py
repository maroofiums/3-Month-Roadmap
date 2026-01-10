from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
import datetime
oauth = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "your_secret"
ALGORITHM = "HS256"
EXPIRE_TIME_MINUTES = 30
fake_user = {
    "username": "admin",
    "password": "admin123"
}
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(EXPIRE_TIME_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(token: str = Depends(oauth)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return {"username": username}
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
