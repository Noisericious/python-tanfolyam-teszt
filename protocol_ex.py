from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class Greeting(Protocol):
    def greet(self, name: str) -> str: ...

class EnglishGreet:
    def greet(self, name: str):
        return f'Hello, {name}!'

class HungarianGreet:
    def greet(self, name: str):
        return f'Szia, {name}!'

def test_greet(g: Greeting, who: str):
    print(g.greet(who))

test_greet(EnglishGreet(), "Elek")
test_greet(HungarianGreet(), "Elek")

obj = HungarianGreet()
print(isinstance(obj, HungarianGreet))
print(isinstance(obj, Greeting))