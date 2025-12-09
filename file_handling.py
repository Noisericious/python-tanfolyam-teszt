import csv
from csv import DictWriter

file_read = open("text.txt","r", encoding="utf-8")
print(file_read.read())
file_read.close()

with open("text.txt","r", encoding="utf-8") as var:
    print(var.read())

with open("text.txt","w", encoding="utf-8") as file:
    file.write("alma\n")
    file.write("barack\n")
    file.write("citrom\n")

with open("text.txt","a", encoding="utf-8") as file:
    file.write("test\n")

with open("text.txt", "r+", encoding="utf-8") as file:
    file.seek(6)
    file.write("###")

with open("test.csv", "r", encoding="utf-8") as file:
    var = csv.reader(file)
    print(var)
    for item in var:
        print(item)

print("-" * 50)

with open("test2.csv", "r", encoding="utf-8") as file:
    var = csv.reader(file, delimiter=";", quoting=csv.QUOTE_NONE)
    print(var)
    for item in var:
        print(item)

print("-" * 50)

csv.register_dialect("valami", delimiter=";", quoting=csv.QUOTE_NONE)
with open("test2.csv", "r", encoding="utf-8") as file:
    var = csv.reader(file, dialect="valami")
    for item in var:
        print(item)

data = [
    [1, 2, 3, "cica"],
    ["egy", "ketto", "harom", "negy"]
]
file = open("test.csv", "w", encoding="utf-8", newline="")
with file:
    w = csv.writer(file)
    w.writerows(data)

with open("test2.csv", "w", encoding="utf-8", newline="") as file:
    w = csv.writer(file, dialect="valami")
    w.writerows(data)

with open("test3.csv", "r", encoding="utf-8", newline="") as file:
    dic_reader = csv.DictReader(file)
    for row in dic_reader:
        print(row["gyümölcs"])

with open("test4.csv", "w", encoding="utf-8", newline="") as file:
    header = ["név", "e-mail", "lakhely"]
    dic_writer = DictWriter(file, fieldnames=header, dialect="valami")
    dic_writer.writeheader()
    dic_writer.writerow({
        "név": "Teszt Elek",
        "e-mail": "teszt@valami.hu",
        "lakhely": "Budapest"
    })

# házi: szerencse program, feladat, ki kell találni oszloponként melyek voltak a leggyakoribb számok. 5 szám kell. oszloponként a leggykoribb.