import asyncio
import time
import aiohttp

URLS = [
    "https://www.python.org",
    "https://www.google.com",
    "https://www.httpbin.org/delay/2",
    "https://github.com"
]


async def check_url(session: aiohttp.ClientSession, url: str):
    print(f"ASSZINKRON lekérés indul: {url}")
    try:
        async with session.get(url) as response:
            print(f"ASSZINKRON {url} -> {response.status}")
    except asyncio.TimeoutError as e:
        print(f"ASSZINKRON Timeout hiba {url} -> {e}")
    except aiohttp.ClientError as e:
        print(f"ASSZINKRON Client hiba {url} -> {e}")

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
            tasks = []
            for url in URLS:
                tasks.append(asyncio.create_task(check_url(session, url)))
            await asyncio.gather(*tasks)

    endTime = time.time()
    print(f"Össz futtatási idő (asszinkron) {endTime - start:.2f} mp")


if __name__ == "__main__":
    asyncio.run(main())
