import asyncio


async def main():
    print('in order')
    task = asyncio.create_task(foo('text'))
    print('Finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())