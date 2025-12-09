gyumolcsok = ["alma", "körte", "banán", "narancs", "eper", "szőlő", "málna", "citrom", "őszibarack"]
zoldsegek = ["krumpli", "répa", "paradicsom", "uborka", "paprika", "káposzta", "hagyma", "sárgarépa", "cékla"]
allatok = ["cica", "kutya", "ló", "elefánt", "tyúk", "kacsa", "tigris", "oroszlán", "kígyó", "malac"]

v1 = input("Írj be valamit: ").lower()  # Kisbetűssé alakítjuk

if v1 in gyumolcsok:
    print("Ez egy gyümölcs")
elif v1 in zoldsegek:
    print("Ez egy zöldség")
elif v1 in allatok:
    print("Ez egy állat")
else:
    print("Sajnos nem tudom, mi ez")
