import asyncio
import time


async def stopper():
    start = time.time()
    while True:
        elapsed = time.time() - start
        print(f"Eltelt idő: {elapsed:.1f} mp")
        await asyncio.sleep(1.0)

async def short_task():
    print("Rövid kis feladat")
    await asyncio.sleep(2)
    print("Rövid feladat vége 2mp")

async def long_task():
    print("Hosszú feladat")
    await asyncio.sleep(9)
    print("hosszú feladat vége 9mp")

async def main():
    stopper_task = asyncio.create_task(stopper())
    short_t = asyncio.create_task(short_task())
    long_t = asyncio.create_task(long_task())

    await asyncio.gather(short_t, long_t)

    stopper_task.cancel()

asyncio.run(main())