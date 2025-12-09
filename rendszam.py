import re

regi_pattern = r"^[A-Z]{3}-\d{3}$"
uj_pattern = r"^[A-Z]{4}-\d{3}$"

while True:
    rendszam = input("Írd be a rendszámot (vagy 'vége' a kilépéshez): ").upper().replace(" ", "")

    if rendszam == "VÉGE":
        print("Kilépés...")
        break


    if re.match(r"^[A-Z]{3}-?\d{3}$", rendszam):
        print(f"→ Régi magyar rendszám ")
    elif re.match(r"^[A-Z]{4}-?\d{3}$", rendszam):
        print(f"→ Új magyar rendszám ")
    else:
        print(f"→ Hibás formátum ")