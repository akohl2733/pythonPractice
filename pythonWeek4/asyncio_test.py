import asyncio

# async def say_hello(name):
#     print(f"Starting task for {name}")
#     await asyncio.sleep(2)
#     print(f"Hello, {name}")

# async def main():
#     await asyncio.gather(
#         say_hello("Alice"),
#         say_hello("Bob"),
#         say_hello("Charlie")
#     )

# asyncio.run(main())

# -----------------------
# import random 

# async def fetch_data(url):
#     delay = random.uniform(1, 3)
#     print(f"Fetching {url} (will take {delay:.2f}s)")
#     await asyncio.sleep(delay)
#     print(f"Done: {url}")
#     return f"Data from {url}"

# async def main():
#     urls = [
#         "https://example.com/a",
#         "https://example.com/b",
#         "https://example.com/c"
#     ]
#     tasks = [fetch_data(url) for url in urls]
#     res = await asyncio.gather(*tasks)
#     print("All results:", res)

# asyncio.run(main())

# ---------------------------------------
import aiohttp


async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Fetched {url} with status {response.status}")
            return data[:100]
    except Exception as e:
        print(f"Error fetching {url}", e)
        return None

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/delay/2",
        "https://jsonplaceholder.typicode.com/posts/1"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    print("\n Results:")
    for i, result in enumerate(results):
        print(f"{i}, {result}\n")

asyncio.run(main())