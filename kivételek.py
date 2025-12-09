try:
    f = open("text.txt", "r")
    f.write("valami")
except FileNotFoundError:
    print("Nincs meg a fájl")
except IOError:
    print("Íráshiba")
except:
    print("kritikus hiba történt")
else:
    print("Siker esetén hajtódik végre")
    f.close()
finally:
    print("Minden esetben lefut")