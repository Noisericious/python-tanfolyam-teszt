import sys
import os

user_input = ""
count_loop = 0
while not user_input.isdigit():
    os.system("cls" if os.name == "nt" else "clear")
    if count_loop > 0:
        print("Rossz adatot adtál meg, csak számokat adj meg!")
    user_input = input("Írj be számokat: (vagy exit, ha ki akar lépni):")
    if user_input.lower() == "exit":
        sys.exit("A kilépést válaszottad, viszlát!")
    count_loop += 1

odd_list = []
even_list = []

for i in user_input:
    if int(i) %2 == 0 and i not in even_list:
        even_list.append(i)
    elif int(i) %2 != 0 and i not in odd_list:
        odd_list.append(i)

if not even_list:
    print("Nincs páros szám benne!")
else:
    if len(even_list) == 1:
        print("A páros számok a következők: %s" %even_list[0])
    else:
        print("A páratlan számok a következők: %s" %even_list)

if not odd_list:
    print("Nincs páros szám benne!")
else:
    if len(odd_list) == 1:
        print("A páratlan számok a következők: %s" %odd_list[0])
    else:
        print("A páratlan számok a következők: %s" %odd_list)



