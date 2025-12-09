from abc import ABC, abstractmethod
from typing import Any, Dict

class Storage(ABC):#spec osztály, olyan, amit majd nem akarok példányosítani, megtiltom, hogy példányosítható legyen.
    @abstractmethod
    def save(self, key: str, value: Any) -> None: ... #nem megvalósított, absztrakt függvény

    @abstractmethod
    def load(self, key: str) -> Any: ...

class MemoryStorage(Storage):
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def save(self, key: str, value: Any) -> None:
        self.data[key] = value

    def load(self, key: str) -> Any:
        return self.data[key]


class FileStorage(Storage):
    def __init__(self, path: str):
        self.path = path

    def save(self, key: str, value: Any) -> None:
        with open(f"{self.path}_{key}.txt", "w", encoding="utf-8") as f:
            f.write(str(value))

    def load(self, key: str) -> Any:
        with open(f"{self.path}_{key}.txt", "r", encoding="utf-8") as f:
            return f.read()

class User:
    def __init__(self, storage: Storage):
        self.storage = storage

    def register(self, username: str):
        self.storage.save("last_user", username)

    def last_registered(self):
        return self.storage.load("last_user")

mem = User(MemoryStorage())
mem.register("Elek")
print("Memoriából: ", mem.last_registered())

file = User(FileStorage("user"))
file.register("Jakab")
print(file.last_registered())

