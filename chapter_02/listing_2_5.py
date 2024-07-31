import asyncio

async def hello_world_message() -> str:
    # asyncio.sleep is a coroutine
    await asyncio.sleep(1)   # 当前协程（hello_world_message）暂停执行，允许其他协程运行
    return "Hello World!"

async def main() -> None:
    # await会暂停当前协程（main），直到被等待的协程（hello_world_message）完成并返回结果
    message = await hello_world_message()
    print(message)

asyncio.run(main())
