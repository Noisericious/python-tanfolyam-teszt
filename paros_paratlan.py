var = input("Adj meg egy számot: ")

paros_szam = ""
paratlan_szam = ""

for szam in var:
    if int(szam) % 2 == 0:
        if szam not in paros_szam:
            paros_szam += szam
    else:
        if szam not in paratlan_szam:
            paratlan_szam += szam

print("Páros számok:", paros_szam)
print("Páratlan számok:", paratlan_szam)
