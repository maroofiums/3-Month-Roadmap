# Async Practice
import asyncio,time

# Sync Example
def sync_func():
    time.sleep(2)

start = time.time()
sync_func()
sync_func()
end = time.time()
print(f"Sync Time: {end - start:.2f} seconds")

# Async Example
async def async_func():
    await asyncio.sleep(2)

async def main():
    await asyncio.gather(async_func(), async_func())
start = time.time()
asyncio.run(main())
end = time.time()
print(f"Async Time: {end - start:.2f} seconds")

# Explanation:
# The synchronous function blocks the execution for 2 seconds each time it's called,
# resulting in a total of approximately 4 seconds.
# The asynchronous function allows both calls to run concurrently,
# resulting in a total of approximately 2 seconds.
