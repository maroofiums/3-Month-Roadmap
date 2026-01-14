from fastapi import FastAPI, Request,Depends
from rate_limiter import rate_limiter

app = FastAPI(description="A simple rate-limited API using FastAPI and Redis.")

@app.get("/public")
async def public_endpoint():
    return {"message": "This is a public endpoint with no rate limiting."}

@app.get("/limited")
async def limited_endpoint(request: Request, _: None = Depends(rate_limiter)):
    return {"message": "This is a rate-limited endpoint."}
