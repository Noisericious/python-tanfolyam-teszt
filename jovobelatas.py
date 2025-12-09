import csv

# Itt tároljuk az összes szám előfordulását
counts = {}

with open("otos.csv", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        numbers = row[-5:]   # Az utolsó 5 oszlop a számok
        for num in numbers:
            num = int(num)
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

# Rendezés gyakoriság alapján (legtöbb elől)
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Az első 5 szám kiírása
top5 = [num for num, db in sorted_counts[:5]]

print("Leggyakoribb 5 szám összesítve:", top5)
