import asyncio

async def download_file(name, seconds):
    print(f"Starting {name}")
    await asyncio.sleep(seconds)
    print(f"Finished {name}")

async def main():
    start = asyncio.get_event_loop().time()
    await asyncio.gather(
        download_file("File1", 2),
        download_file("File2", 2),
        download_file("File3", 2),
    )
    print(f"Async took {asyncio.get_event_loop().time() - start:.2f} seconds")

asyncio.run(main())