from fastapi import FastAPI
from app.routers.users import router

app = FastAPI()

app.include_router(router)

