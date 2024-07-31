# this code dose not operate differently from normal sequential code 
import asyncio
import time

async def add_one(number: int) -> int:
    time.sleep(10)
    print(f"the number is {number}")
    return number + 1


async def main() -> None:
    # pause the main function until getting the result of add_one(1) 
    one_plus_one = await add_one(1)
    # pause the main function until getting the result of add_one(2) 
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())
