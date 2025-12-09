def first_decorator(fn):
    def inner_fn():
        print("Dekorator fgv vagyok")
        fn()
    return inner_fn

def simple_fn():
    print("Ez egy sima fgv")

d = first_decorator(simple_fn)
d()

@first_decorator
def simple_fn2():
    print("Ez egy sima fgv 2")

simple_fn2()


print("-" * 50)

def divide_decorator(fn):
    def inner_fn(a, b):
        print("Elosztok egymással két számot, az ", a, "és a ", b, " számot")
        if b == 0:
            print("Nem lehet 0-val osztani!")
            return
        return fn(a, b)
    return inner_fn

@divide_decorator
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))


def star(fn):
    def inner(*args, **kwargs):
        print("*" * 50)
        fn(*args, **kwargs)
        print("*" * 50)
    return inner

def equals(fn):
    def inner(*args, **kwargs):
        print("=" * 50)
        fn(*args, **kwargs)
        print("=" * 50)
    return inner

@star
@equals
def disp1(v1):
    print(v1)

@star
@equals
def disp2(v1, v2):
    print(v1)
    print(v2)

disp1("alma")
disp2(1, 2)





