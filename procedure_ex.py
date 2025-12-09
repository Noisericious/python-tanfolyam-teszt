# def utána név, zárójelben, fölvesszük a paramétereket, és : követően az utasítások jönnek
# def fgv_neve(PRAMETER):
#    utasítások

def first(name):
    """
    ez a fgv köszön
    """
    print("Hello " + name)

first("Elek")
print(first.__doc__)

def second(num):
    if num %2 == 0:
        return "Páros a szám"
        print("ok")
    return "Nem páros a szám"

print(second(3))
print(second(4))

def third(num):
    return num * num

var1 = lambda num: num * num

print(third(3))
print(var1(3))

print(third.__name__)
print(var1.__name__)

var2 = lambda a, b: a + b
print(var2(1, 2))

users = [
    {"username": "Elek", "email": "teszt@elek.hu", "orders": ["T1", "T2", "T3"]},
    {"username": "Jakab", "email": "teszt@jakab.hu", "orders": []},
    {"username": "Feri", "email": "teszt@feri.hu", "orders": []},
    {"username": "Pista", "email": "teszt@pista.hu", "orders": ["T4", "T5", "T6"]},
    {"username": "Bela", "email": "teszt@bela.hu", "orders": []},
    {"username": "Mari", "email": "teszt@mari.hu", "orders": ["T1", "T2", "T3"]},
]

if __name__ == "__main__":
    #nincs rendelése
    wo_users = list(filter(lambda u: not u["orders"], users))
    print(wo_users)

    wo_users2 = [user for user in users if not user["orders"]] #ugyan az, csak listával
    print(wo_users2)

    user_names = list(map(lambda user: user["username"].upper(), users))
    print(user_names)

    user_names = list(map(lambda user: user["username"].upper(), filter(lambda u: not u["orders"], users)))
    print(user_names)

    user_names2 = [user["username"].upper() for user in users if not user["orders"]] #ugyan az csak listával
    print(user_names2)

#házi gömb térfogatának kiszámítása függvénnyel.
#fgv ami kiírja, ha átadunk neki 3 számot pl. 6,3,9, kiírja, hogy a 6os a 3-as 9 között van. de ha 6 7 9 a három szám,akkor 6-os nincs a 9 között.
#fgv ami kiírja a nagy és kisbetűk számát egy átadott szövegben
#fgv ami egy átadott listában megszünteti a duplikációkat
#írjunk egy olyan fgv ami pangram-e az átadott szó (abc összeds betűje megtalálható)
#fgv, palindrom-e az átadott szó
