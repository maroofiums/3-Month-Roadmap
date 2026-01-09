import time
from fastapi import Request
from auth import get_current_user

async def log_request_middleware(request: Request, call_next):
    
    start_time = time.time()

    token = request.headers.get("Authorization")
    user = None
    if token:
        try:
            user = await get_current_user(token)
        except Exception:
            user = None
    response = await call_next(request)
    process_time = time.time() - start_time

    print(f"Request: {request.method} {request.url} | User: {user} | Process Time: {process_time:.4f} seconds")

    return response


