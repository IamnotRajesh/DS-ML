import asyncio
import aiohttp
from timer import timer
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

URL = "https://httpbin.org/uuid"

async def fetch_uuid(session, url):
    async with session.get(url) as response:
        json_data = await response.json()
        print(response.json()['uuid'])

async def func():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_uuid(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)

@timer(1,1)
async def run():
    asyncio.run(func())



#if __name__ == '__main__':
    # Without concurrency control
    #timer(lambda: asyncio.run(main()))
    
    # With concurrency control (using ThreadPoolExecutor)
#    executor = Pool(5)   # Adjust this number to your system's capabilities
 #   timer(lambda: executor.run(asyncio.run(main)))   # Run the function inside the executor</s>