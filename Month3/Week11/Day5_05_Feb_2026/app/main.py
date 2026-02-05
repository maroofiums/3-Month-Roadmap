from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random,string

app = FastAPI()

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(10), unique=True, index=True)
    long_url = Column(Text, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

class URLRequest(BaseModel):
    long_url: str

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.post("/shorten/")
def shorten_url(url_request: URLRequest):
    db = SessionLocal()

    short_code = generate_short_code()

    url = URL(
        short_code=short_code,
        long_url=url_request.long_url
    )
    db.add(url)
    db.commit()
    db.refresh(url)

    return {
        "short_url": f"http://localhost:8000/{short_code}",
        "long_url": url.long_url
    }

@app.get("/{short_code}")
def redirect_url(short_code: str):
    db = SessionLocal()
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url.long_url)
