# szia hogy vagy ma
# m
# ma
# ma
# ma va
# ma vagy hogy szia

var = input("Írjon be egy szöveget: ")
list1 = var.split(" ")
list1.reverse()
string1 = " ".join(list1)
output = ""
for c in string1:
    output += c
    print(output)

