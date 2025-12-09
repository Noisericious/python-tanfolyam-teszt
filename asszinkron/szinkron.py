import random
import time


def szinkron(n: int):
    print(f"Szinkron feladat fut {n}")
    sleep_time = random.uniform(0.5, 2.0)
    time.sleep(sleep_time)
    print(f"Szinkron feladat befejeződött {n} ({sleep_time: .2f} mp)")

def main():
    start = time.time()

    for i in range(1, 4):
        szinkron(i)

    end_time = time.time()
    print(f"Össz futtatási idő {end_time - start:.2f} mp")

main()