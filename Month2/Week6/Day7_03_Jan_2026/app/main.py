from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import Column,Integer,String,select
app = FastAPI()

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL,echo=True)

async_session = sessionmaker(
    engine ,expire_on_commit=False,class_ = AsyncSession
)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

import asyncio
asyncio.run(init_models())

async def get_db():
    async with async_session() as session:
        yield session

@app.post("/add_user")
async def add_user(name: str, db: AsyncSession = Depends(get_db)):
    user = User(name=name)
    db.add(user)
    await db.commit()
    return {"message": "User added"}

@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)