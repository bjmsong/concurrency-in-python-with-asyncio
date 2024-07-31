import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1

# asyncio.run: abstract the event loop management, run the coroutine
# 1. create a brand-new event
# 2. run the coroutine until it completes, return the result
# 3. cleanup
# 4. shut down, close the event loop
result = asyncio.run(coroutine_add_one(1))

print(result)
