import asyncio

async def task1():
    print('Send 1st email')
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print('1st Email reply')

async def task2():
    print('Send 2nd email')
    asyncio.create_task(task3())
    await asyncio.sleep(3)
    print('2nd Email reply')

async def task3():
    print('Send 3rd email')
    await asyncio.sleep(1)
    print('3rd Email reply')

asyncio.run(task1())