from fastapi import Request, HTTPException
from redis_client import redis_client

RATE_LIMIT = 5
WINDOW = 10

def rate_limiter(request: Request):
    ip = request.client.host
    key = f"rate:{ip}"

    count = redis_client.get(key)

    if count is None:
        redis_client.set(key, 1, ex=WINDOW)
        return

    if int(count) >= RATE_LIMIT:
        raise HTTPException(429, "Too many requests")

    redis_client.incr(key)
