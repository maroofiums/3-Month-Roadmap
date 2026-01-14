from fastapi import HTTPException,Request
from redis_client import redis_client

RATE_LIMIT = 3
TIME_WINDOW = 60  

def rate_limiter(request: Request):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    current_count = redis_client.get(key)

    if current_count is None:
        redis_client.set(key, 1, ex=TIME_WINDOW)
        return
    
    elif int(current_count) < RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later."
        )
    
    redis_client.incr(key)

    