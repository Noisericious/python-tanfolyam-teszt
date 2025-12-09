# 1. adatbetöltés fájlból
# 2. új rendelés felvitele
# 3. rendelés módosítása
# 4. rendelés megtekintése
# 5. rendelés mentése
# 6. rendelés törlése
# 7. statisztika
import csv
import json
from collections import Counter
from datetime import datetime

MENU_FILE = "menu.csv"
ORDERS_FILE = "orders.json"

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} Ft"

    def to_dict(self):
        return {"name": self.name, "price": self.price}


class Order:
    def __init__(self, customer_name: str, table_number: int, items: list[MenuItem]):
        self.customer_name = customer_name
        self.table_number = table_number
        self.items = items
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def total_price(self):
        return sum(int(item.price) for item in self.items)

    def __str__(self):
        item_names = ", ".join(item.name for item in self.items)
        return f"Vendeg: {self.customer_name}, Asztal: {self.table_number}, Tételek: {item_names}, Total: {self.total_price()} Ft, Time: {self.timestamp}"

    def to_dict(self):
        return {"customer_name": self.customer_name,
                "table_number": str(self.table_number),
                "items": [item.to_dict() for item in self.items],
                "timestamp": self.timestamp
        }


def load_menu():
    menu = []
    try:
        with open(MENU_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(MenuItem(row["name"], row["price"]))
    except FileNotFoundError:
        print("Menu file nem található! Ellenőrizd, hogy a menu.csv megtalálható-e a program mellett.")
    except:
        print("Kritikus hiba a menu betöltése közben!")
    return menu


def save_orders(orders):
    try:
        with open(ORDERS_FILE, mode="w", encoding="utf-8") as file:
            json.dump([order.to_dict() for order in orders], file)
    except TypeError as err:
        print("KRITIKUS HIBA!")
        print(err)


def load_orders():
    orders = []
    try:
        with open(ORDERS_FILE, mode="r", encoding="utf-8") as file:
            orders_dict = json.load(file)
            for order_item in orders_dict:
                items = [MenuItem(item["name"], item["price"]) for item in order_item["items"]]
                order = Order(order_item["customer_name"], int(order_item["table_number"]), items)
                order.timestamp = order_item["timestamp"]
                orders.append(order)
    except FileNotFoundError:
        print("Rendelés file nem található. Ellenőrizd, hogy létezik-e a rendelés json file!")
    except:
        print("KRITIKUS HIBA!")
    return orders


def list_menu(menu):
    print("=== Menu ===")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item}")

def take_order(menu: list[MenuItem]):
    print("=== Rendelés ===")
    customer_name = input("Vendég neve: ")
    table_number = input("Asztal száma: ")
    list_menu(menu)
    items = []
    while True:
        choice = input("Kérem válasszon a szám alapján (Ha nem akar mást rendelni nyomjon Entert):")
        if not choice:
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(menu):
            items.append(menu[int(choice) - 1])
        else:
            print("Rossz számot adtál meg, próbáld újra!")
    return Order(customer_name, int(table_number), items)


def list_orders(orders):
    print("=== Jelenlegi rendelések ===")
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order}")


def delete_order(orders):
    list_orders(orders)
    choice = input("Válasszon ki egy rendelést a törléshez: ")
    if choice.isdigit() and 1 <= int(choice) <= len(orders):
        del orders[int(choice) - 1]
        print("A rendelés törölve.")
    else:
        print("A rendelés száma nem megfelelő, így nem tudjuk teljesíteni.")


def generate_statistics(orders):
    if not orders:
        print("Nincs megrendelés a statisztika generálásához.")
        return
    total_income = sum(order.total_price() for order in orders)
    all_items = [item.name for order in orders for item in order.items]
    most_popular_item = Counter(all_items).most_common(1)[0][0]
    print(f"Teljes bevétel: {total_income} Ft")
    print(f"A legnépszerűbb étel: {most_popular_item} ")


def main():
    menu = load_menu()
    orders = load_orders()

    while True:
        print("=== Éttermi alkalmazás ===")
        print("1. menu listázása")
        print("2. új rendelés felvétele")
        print("3. rendelés listázása")
        print("4. rendelés törlése")
        print("5. statisztika")
        print("6. mentés és kilépés")

        choice = input("vállaszon egy elemet: ")
        if choice == "1":
            list_menu(menu)
        elif choice == "2":
            order = take_order(menu)
            orders.append(order)
        elif choice == "3":
            list_orders(orders)
        elif choice == "4":
            delete_order(orders)
        elif choice == "5":
            generate_statistics(orders)
        elif choice == "6":
            save_orders(orders)
            print("Rendelés sikeresen leadva. Kilépés...")
            break
        else:
            print("Ilyen lehetőség nincs!")


if __name__ == "__main__":
    main()

# házi feladat: bármilyen korábbi programot class-okkal, hierarchikus módon megcsinálni.
















