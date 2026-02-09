from sqlmodel import select
from velox.db import VeloxDB
from sqlmodel.ext.asyncio.session import AsyncSession

class VeloxCRUD:
    def __init__(self, db: VeloxDB):
        self.db = db

    async def create(self, model, data: dict):
        async with AsyncSession(self.db.engine) as session:
            obj = model(**data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def get(self, model, obj_id: int):
        async with AsyncSession(self.db.engine) as session:
            result = await session.get(model, obj_id)
            return result

    async def update(self, model, obj_id: int, data: dict):
        async with AsyncSession(self.db.engine) as session:
            obj = await session.get(model, obj_id)
            if not obj:
                return None
            for key, value in data.items():
                setattr(obj, key, value)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, model, obj_id: int):
        async with AsyncSession(self.db.engine) as session:
            obj = await session.get(model, obj_id)
            if not obj:
                return False
            await session.delete(obj)
            await session.commit()
            return True
