print("{0:^10} | {1} | {2:^10}".format("Kosár", "Mennyiség", "Bolt"))
print("-" *35)
print("{0:^10} | {1:^9} | {2:^10}".format("alma", "3kg", "Lidl"))
print("{0:^10} | {1:^9} | {2:^10}".format("citrom", "1kg", "Spar"))
print("{0} | {1:^9} | {2:^10}".format("paradicsom", "2kg", "Aldi"))
a1 = "alma"
b1 = "citrom"
c1 = "paradicsom"
print("{} | {} | {}".format(a1, b1, c1))

print("A szám: {0:10.2f}".format(12.123456))



s1="viki"
print(s1)
print(s1.upper())

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
matrix1 = [list1, list2, list3]
print([matrix1[cv] for cv in [0, 2]])
print([item[0] for item in [matrix1[cv] for cv in [0, 2]]])
print([matrix1[i] for i in [0, 2]])
print([[row[i] for i in [0, 2]] for row in matrix1])

