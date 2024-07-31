import asyncio
import sys
import os
sys.path.append(os.getcwd())
from util import delay


async def add_one(number: int) -> int:

    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


async def main() -> None:
    # hello_world_message()和add_one()仍然是串行执行的
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(message)
    print(one_plus_one)

asyncio.run(main())
