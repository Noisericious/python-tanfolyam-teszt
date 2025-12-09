import csv
import random


class Wordlist:
    def __init__(self, source="szokereso.csv"):
        self.words = self.load_from_csv(source)

    def load_from_csv(self, filename):
        words = []
        try:
            with open(filename, newline='', encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        words.append(row[0].strip().upper())
        except FileNotFoundError:
            print("A szokereso.csv file nem található")
        return words


class Grid:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]

    def create_empty_grid(self, word):
        directions = ["horizontal", "vertical", "diagonal"]
        placed = False
        while not placed:
            direction = random.choice(directions)
            start_row = random.randint(0, self.size - 1)
            start_col = random.randint(0, self.size - 1)

            if direction == "horizontal" and start_col + len(word) <= self.size:
                pass



