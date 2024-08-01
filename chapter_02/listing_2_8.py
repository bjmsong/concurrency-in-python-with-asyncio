import asyncio
import os
import sys
sys.path.append(os.getcwd())
from util import delay


async def main():
    # create a Task Object
    # schedule rountine(delay(3)) to run on the event loop immediately
    # non-blocking fashion: execute other code instantly
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)

asyncio.run(main())
