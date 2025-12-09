print(list("abcdefgh"))
print(list(enumerate("abcdefgh")))

for (i, letter) in enumerate(list("abcdefgh")):
    print(i)

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]

print(list(zip(list1, list2))) #sokat fogjuk ezeket használni

for i in range(0, 6):
    print("{0:>{1}}".format("*", i))

list3 = [x ** 2 for x in range(0, 11)]
print(list3)
