import csv
from collections import Counter

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

csv.register_dialect("lotto", delimiter=";", quoting=csv.QUOTE_NONE)
with open('otos.csv', "r", encoding='utf-8', newline='') as file:
    csv_reader = csv.reader(file, dialect="lotto")
    for row in csv_reader:
        list1.append(row[-5])
        list2.append(row[-4])
        list3.append(row[-3])
        list4.append(row[-2])
        list5.append(row[-1])

first = Counter(list1)
second = Counter(list2)
third = Counter(list3)
fourth = Counter(list4)
fifth = Counter(list5)

print(first.most_common(1)[0][0] + ", " + second.most_common(1)[0][0] + ", " + third.most_common(1)[0][0] + ", " + fourth.most_common(1)[0][0] + ", " + fifth.most_common(1)[0][0])
