def summarize(*args):
    return sum(args)

print(summarize(1, 2, 3))
print(summarize(4, 5, 6, 7, 8, 9))

def ex_fn(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

ex_fn(nev="Elek", kor=22, varos="Budapest")

def ex_fn2(item, *args, **kwargs):
    print(f"Paraméter: {item}")
    print("Args, argumentum: ", args)
    print("Kwargs, argumentum: ", kwargs)

ex_fn2("alma", 1,2,3, nev="Jakab", kor=55)

def receive(*args, **kwargs):
    print("Args", args)
    print("Kwargs:", kwargs)

def send(*args, **kwargs):
    receive(*args, **kwargs)

send("alma", 1,2,3, nev="Jakab", kor=55)


