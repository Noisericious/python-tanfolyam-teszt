import csv

stat = [{}, {}, {}, {}, {}]

with open("otos.csv", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        numbers = row[-5:]
        for i, num in enumerate(numbers):
            num = int(num)
            if num not in stat[i]:
                stat[i][num] = 0
            stat[i][num] += 1

#print(stat[0])
#print(stat[1])
#print(stat[2])
#print(stat[3])
#print(stat[4])

most_frequent = []
for col in stat:
    most_common_num = None
    highest_count = 0
    for num in col:
        #print("num is: ", num)
        #print("value is: ", col[num])
        if col[num] > highest_count:
            highest_count = col[num]
            most_common_num = num
    most_frequent.append(most_common_num)

print("Leggyakoribb számok oszloponként:", most_frequent)