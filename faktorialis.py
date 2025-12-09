#5! = 5 * 4 * 3 * 2 *1

var = int(input("Melyik szám faktoriálisát keresed? "))
original_value = var
str1 = ""
fac = 1

while  var != 0:
    str1 = str1 + str(var) + " * "
    fac = fac * var
    var -= 1

print("A faktoriáli a %s számnak (%s! = %s)) az %s" %(original_value, original_value, str1[:-3], fac))


