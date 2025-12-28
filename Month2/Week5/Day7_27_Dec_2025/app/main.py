from fastapi import FastAPI
from Week5.Day7_27_Dec_2025.app.routers.todo import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)