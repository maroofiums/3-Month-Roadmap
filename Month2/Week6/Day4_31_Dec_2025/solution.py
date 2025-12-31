from fastapi import FastAPI
import asyncio
app = FastAPI()

def fake_db_call():
    asyncio.sleep(3)
    return {
        {"id":1,"name":"John Doe"},
        {"id":2,"name":"Jane Smith"}
    }


@app.get("/data")
async def get_data():
    data = await fake_db_call()
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    