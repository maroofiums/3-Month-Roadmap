from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import engine, Base
from routes import router
from auth import create_token

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Todo API with Auth", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Login credentials (in production, use proper user database)
DEMO_USERS = {
    "admin": "password123",
    "user": "user123"
}

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(credentials: LoginRequest):
    """Login endpoint - returns JWT token"""
    if credentials.username not in DEMO_USERS:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if DEMO_USERS[credentials.username] != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token({"sub": credentials.username})
    return {"access_token": token, "token_type": "bearer"}

# Include routes
app.include_router(router)

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Todo API with Authentication"}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
