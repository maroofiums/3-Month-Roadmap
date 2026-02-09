from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

class VeloxDB:
    def __init__(self, db_url="sqlite+aiosqlite:///db.sqlite3"):
        # Async engine
        self.engine = create_async_engine(db_url, echo=True, future=True)

    async def init_db(self):
        # Auto-create tables
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    def get_session(self):
        # Returns a new AsyncSession
        return AsyncSession(self.engine, expire_on_commit=False)
