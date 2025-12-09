import asyncio
import random
import time


async def work(id: int, sema: asyncio.Semaphore):
    async with sema:
        print(f"Munka {id} elindult")
        await asyncio.sleep(random.uniform(1, 5))
        print(f"Munka {id} kilépett a feldolgozásból")

async def main():
    start = time.time()
    sema = asyncio.Semaphore(3)

    tasks = [
        asyncio.create_task(work(i, sema)) for i in range(1, 21)
    ]

    await asyncio.gather(*tasks)
    endTime = time.time()
    print(f"Összesen: {endTime - start:.2f} mp")

if __name__ == "__main__":
    asyncio.run(main())