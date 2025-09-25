import asyncio

async def fetch_data(n):
    print(f"Fetching {n}")
    await asyncio.sleep(1)
    print(f"Done {n}")
    return n

async def main():
    for i in range(3):
        fetch_data(i)

    print("Now concurrent:")
    results = await asyncio.gather(*(fetch_data(i) for i in range(3)))
    print("Results:", results)

asyncio.run(main())