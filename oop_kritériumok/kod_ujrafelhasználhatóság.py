import json
from datetime import datetime
from typing import Protocol


class JsonSerializeMixin:
    def to_dict(self) -> dict:
        result = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (str, int, float, bool)) or v is None:
                result[k] = v
            elif isinstance(v, datetime):
                result[k] = v.isoformat(timespec="seconds")
            else:
                result[k] = str(v)
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

class TimeStampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

# interjún: van egy olyan elnevezés pythonban, hogy protocol:
# leegyszerűsítve egy leírást jelent, arról, hogy ha felveszünk valamit, milyen metódusok kellenek, hogy egy objektumot elfogadjunk.

class Discount(Protocol):
    def __call__(self, amount: int) -> float: ...

class PercentageOff:
    def __init__(self, percent: float):
        self.percent = percent

    def __call__(self, amount: int) -> float:
        return amount * (1 - self.percent / 100)

class FlatOff:
    def __init__(self, amount_off):
        self.amount_off = amount_off

    def __call__(self, amount: int) -> float:
        return amount - self.amount_off

class Customer(JsonSerializeMixin, TimeStampMixin):
    def __init__(self, name: str, email: str):
        super().__init__()
        self.name = name
        self.email = email

class Order(JsonSerializeMixin, TimeStampMixin):
    def __init__(self, customer: Customer, price: int, discount: Discount):
        super().__init__()
        self.customer = customer
        self.price = price
        self.discount_price = discount(price)

cust = Customer("Elek", "elek@tesztelek.hu")
order = Order(cust, 10000, PercentageOff(15))
print(order.to_json())






