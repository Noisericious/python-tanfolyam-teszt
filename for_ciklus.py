#for ciklus_változó in kollekció, amit be szeretnénk járni:
#    CM

list1 = [1,2,3,4,5,6,7,8,9]
for item in list1:
    if item %2 == 0:
        print(item)

sum = 0
for item in list1:
    sum = item + sum

print("az össszeg: " + str(sum))

for item in "Ez egy szöveg":
    print(item)

t1 = (1,2,3,4,5,6,7,8,9)
for t in t1:
    print(t)

list2 = [(2,4), (6,8), (10,12)]
for tup in list2:
    print(tup)

for (tup1, tup2) in list2:
    print("első érték: " + str(tup1))
    print("második érték: " + str(tup2))

dic1 = {"k1": 1, "k2": 2, "k3": 3, "k4": 4}

for (k, v) in dic1.items():
    print(k)
    print(v)

for val in dic1.values():
    print(val)



