import os
import sys #az impotok mindig a fájl elején legyenek, és minden import külön sorban legyen!

def long_method_name(variable_one, variable_two,
                     variable_three, variable_four):
    print(variable_two) #ha elnevezek egy fgvt és több argumentuma van, ami szintén hosszú, akkor egy sok hossza max 79 karakter legyen és törjük a sort

#változó nevek, fgv nevek userAge = 33 (def) ne a hungarian notésönt használd, snake case tehát user_age = 33
user_age = 33 #helyes
userAge = 33
age = 33

b = 1
c = 2
a=b+c #helytelen
a = b + c #helyes

total = (b * c) + (a * b) + (a * c) + (a * a) + \
        (a * a) + (a * a) + (a * a) + (a * a) #erre is vonatkozik a tördelés

def fn1():
    import base64
    print("")


# rövid egysoros fgv helyett lambda, anonim fgv

#short if
print("pozitiv") if age > 0 else print("negativ")

# TODO: valamit még meg kell csinálni
