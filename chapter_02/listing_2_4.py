# this code dose not operate differently from normal sequential code 
import asyncio
import time

async def add_one(number: int) -> int:
    # run asyncio.sleep(5) coroutine, pause the add_one() coroutine until asyncio.sleep(5) is done
    await asyncio.sleep(5)
    print(f"the number is {number}")
    return number + 1


async def main() -> None:
    # run add_one(1) coroutine, pause the main() coroutine until getting the result of add_one(1) 
    one_plus_one = await add_one(1)
    # run add_one(2) coroutine, pause the main() coroutine until getting the result of add_one(2) 
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())
