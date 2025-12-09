import csv

stat = [{} for _ in range(5)]

with open("otos.csv", "r", newline="", encoding="utf-8") as file:
    dic_reader = csv.DictReader(file, delimiter=";")
    for row in dic_reader:
        numbers = row[:-5]
        print(numbers)






