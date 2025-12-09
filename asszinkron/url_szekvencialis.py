import time

import requests

URLS = [
    "https://www.python.org",
    "https://www.google.com",
    "https://www.httpbin.org/delay/2",
    "https://github.com"
]

def check_url(url: str):
    print(f"SZINKRON lekérés indul: {url}")
    try:
        response = requests.get(url)
        print(f"SZINKRON {url} -> {response.status_code}")
    except requests.RequestException as e:
        print(f"SZINKRON hiba {url} -> {e}")

def main():
    start = time.time()
    for url in URLS:
        check_url(url)

    endTime = time.time()
    print(f"Össz futtatási idő (szinkron) {endTime - start:.2f} mp")

if __name__ == "__main__":
    main()
    