from fastapi import FastAPI
import asyncio,time

app = FastAPI()
@app.get("/sync")
def read_sync():
    time.sleep(3)
    return {"message": "This is a synchronous endpoint"}

@app.get("/async")
async def read_async():
    await asyncio.sleep(3)  
    return {"message": "This is an asynchronous endpoint"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

