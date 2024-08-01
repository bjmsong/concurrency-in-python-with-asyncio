from asyncio import Future

# contains a value that you expect to get at some point in the future
my_future = Future()

print(f'Is my_future done? {my_future.done()}')

my_future.set_result(42)

print(f'Is my_future done? {my_future.done()}')
print(f'What is the result of my_future? {my_future.result()}')
