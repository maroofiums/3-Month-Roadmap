from fastapi import FastAPI,HTTPException,Request
import redis

app = FastAPI()

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

RATE_LIMIT = 10
WINDOW_SIZE = 60

@app.get("/data")
def get_data(request:Request):
    user_id = request.client.host
    key = f"User:{user_id}"

    count = redis_client.incr(key)

    if count == 1:
        redis_client.expire(key, WINDOW_SIZE)

    if count > RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )
    
    return {
        "message": "Data retrieved successfully",
        "request_count": count,
        "key": key
    }