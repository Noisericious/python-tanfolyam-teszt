import asyncio
import os
import threading
import time
from asyncio import create_task
from multiprocessing import Process
from multiprocessing.spawn import freeze_support


def cpu_bound_test(task_id: int, n: int):
    print(f"[CPU] task {task_id} START threading {threading.current_thread().name}, PID: {os.getpid()}")
    s = 0
    for i in range(n):
        s += i * i
    print(f"[CPU] task {task_id} END threading {threading.current_thread().name}, PID: {os.getpid()}")

def run_sync_cpu(num_tasks = 4, n = 30000000):
    print("=== SZINKRON VERZIÓ ===")
    start = time.time()
    results = []
    for i in range(1, num_tasks + 1):
        results.append(cpu_bound_test(i, n))

    total = time.time() - start
    print(f"[SZINKRON] össz futási idő: {total:.2f} mp")

async def async_cpu_wrapper(task_id: int, n: int):
    return cpu_bound_test(task_id, n)

async def run_async_cpu(num_tasks = 4, n = 30000000):
    print("=== ASSZINKRON VERZIÓ ===")
    start = time.time()
    tasks = []
    for i in range(1, num_tasks + 1):
        tasks.append(asyncio.create_task(async_cpu_wrapper(i, n)))

    await asyncio.gather(*tasks)
    total = time.time() - start
    print(f"[ASSZINKRON] össz futási idő: {total:.2f} mp")

def run_threaded_cpu(num_tasks = 4, n = 30000000):
    print("=== THREADES VERZIÓ ===")
    start = time.time()
    threads = []
    for i in range(1, num_tasks + 1):
        t = threading.Thread(target=cpu_bound_test, args=(i, n))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = time.time() - start
    print(f"[THREADES] össz futási idő: {total:.2f} mp")


def run_multiprocessing_cpu(num_tasks = 4, n = 30000000):
    print("=== MULTIPROCESSING VERZIÓ ===")
    start = time.time()

    process = []
    for i in range(1, num_tasks + 1):
        p = Process(target=cpu_bound_test, args=(i, n))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    total = time.time() - start
    print(f"[MULTIPROCESSING] össz futási idő: {total:.2f} mp")

def main():
    run_sync_cpu()
    asyncio.run(run_async_cpu())
    run_threaded_cpu()
    run_multiprocessing_cpu()

if __name__ == "__main__":
    freeze_support()
    main()




