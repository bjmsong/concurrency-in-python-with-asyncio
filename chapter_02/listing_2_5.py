import asyncio

async def hello_world_message() -> str:
    await asyncio.sleep(1)   # 模拟一个长时间的操作，当前协程（hello_world_message）暂停执行，允许其他协程运行
    return "Hello World!"    # 1秒后，函数返回字符串"Hello World!"

async def main() -> None:
    # await会暂停当前协程（main），直到被等待的协程（hello_world_message）完成并返回结果
    # 这里如果不加await，返回的是协程对象，而不是计算结果
    message = await hello_world_message()
    print(message)

asyncio.run(main())  # 启动异步事件循环
