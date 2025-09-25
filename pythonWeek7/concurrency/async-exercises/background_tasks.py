import asyncio

async def background_task():
    await asyncio.sleep(3)
    print("Background task finished!")

async def main():
    task = asyncio.gather(background_task())
    print('Doing something else...')
    await asyncio.sleep(1)
    print("Still working...")
    await task

asyncio.run(main())