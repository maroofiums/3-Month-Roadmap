import asyncio

async def tasks(name,delay):
    print(f"Task {name}: Starting with delay {delay}")
    await asyncio.sleep(delay)
    print(f"Task {name}: Completed after {delay} seconds")

async def main():
    task1 = asyncio.create_task(tasks("A", 2))
    task2 = asyncio.create_task(tasks("B", 3))
    task3 = asyncio.create_task(tasks("C", 1))

    await task1
    await task2
    await task3
    
if __name__ == "__main__":
    asyncio.run(main())
