from fastapi import FastAPI,BackgroundTasks
import asyncio

app = FastAPI()
def write_log(message: str):
    with open("log.txt","a") as f:
        f.write(message + "\n")
    

@app.post("/create-item/")
async def create_item(item: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Item created: {item}")
    return {"message": f"Item '{item}' created successfully."}

def async_log(message: str):
    async def log():
        await asyncio.sleep(1) 
        with open("async_log.txt", "a") as f:
            f.write(message + "\n")
    return log()

@app.post("/create-async-item/")
async def create_async_item(item: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(async_log, f"Async item created: {item}")
    return {"message": f"Async item '{item}' created successfully."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)

