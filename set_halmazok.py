s1 = set()
s1.add(1)
s1.add(2)
print(s1)
s2 = {4, "alma", 44}
print(s2)
list1 = [1, 2, 3, 2, 65, 4, 6 , 5, 6, 7, 8, 9, 10, 11]
list2 = list(set(list1))
print(list2)
s2.discard("alma")
print(s2)
s2.remove(44)
print(s2)


print(range(2, 10))
print(list(range(2, 10)))
print(range(2, 10, 2)[1])
#print(range(0, 1000000)) végtelen számot lehet véges adattal tárolni, csak számot
