from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import HTTPException,Depends

oauth = OAuth2PasswordBearer(tokenUrl="/login")

ALGO = "HS256"
EXPIRE_IN_MINUTES = 30
Key = "THis is a secret key"

def create_token(data: dict):
    to_encode = data.copy()
    encode_jwt = jwt.encode(to_encode,Key,algorithm=ALGO)
    return encode_jwt

async def get_current_user(token: str = Depends(oauth)):
    try:
        payload = jwt.decode(token,Key,algorithms=[ALGO])
        return payload

    except jwt.JWTError:
        raise HTTPException(status_code=401,detail="Invalid token")

