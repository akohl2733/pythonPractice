import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    urls = {
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",       
    }
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch_url(session, url) for url in urls))
    print(f"Fetched {len(results)} pages.")

asyncio.run(main())