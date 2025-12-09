import random
import os

def create_grid(size):
    """Creates an empty grid"""
    return [[" " for _ in range(size)] for _ in range(size)]

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def place_word(grid, word):
    """Places a word on the grid in random direction"""
    size = len(grid)
    directions = [(1,0),(0,1),(1,1),(-1,1)]
    word = word.upper()

    for _ in range(1000):
        dx, dy = random.choice(directions)
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)

        end_x = x + dx*(len(word)-1)
        end_y = y + dy*(len(word)-1)
        if not (0 <= end_x < size and 0 <= end_y < size):
            continue

        can_place = True
        for i in range(len(word)):
            if grid[y + i*dy][x + i*dx] != " " and grid[y + i*dy][x + i*dx] != word[i]:
                can_place = False
                break

        if can_place:
            for i in range(len(word)):
                grid[y + i*dy][x + i*dx] = word[i]
            return (x, y, dx, dy)
    print(f"Nem sikerült elhelyezni: {word}")
    return None

def fill_random_letters(grid):
    """Fill empty spaces with random letters"""
    alphabet = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                grid[y][x] = random.choice(alphabet)

def print_grid(grid, highlight=None):
    """Prints the grid with highlighted positions"""
    if highlight is None:
        highlight = set()
    size = len(grid)
    print("    " + " ".join(f"{i:2}" for i in range(1, size+1)))
    print("   " + "---"*size)
    for y, row in enumerate(grid):
        line = ""
        for x, ch in enumerate(row):
            if (x,y) in highlight:
                line += f"[{ch}]"
            else:
                line += f" {ch} "
        print(f"{y+1:2} |{line}")

def main():
    size = 12
    grid = create_grid(size)

    words = ["AUDI", "MERCEDES", "OPEL", "VOLVO", "TOYOTA", "PEUGEOT",
             "TESLA", "ZSIGULI", "SUZUKI", "BUGATTI", "FERRARI"]
    word_positions = {}

    for word in words:
        pos = place_word(grid, word)
        if pos:
            word_positions[word] = pos

    fill_random_letters(grid)

    found_words = set()
    found_positions = set()

    while len(found_words) < len(words):
        clear_screen()
        print("Szókereső játék!")
        print_grid(grid, found_positions)
        print("\nMegtalált szavak:", ", ".join(sorted(found_words)) if found_words else "Még nincs megtalált szó")

        guess = input("\nMelyik szót találtad meg? (vagy 'kilep'): ").strip().upper()
        if guess == "KILEP":
            break
        if guess not in word_positions:
            print("Ez a szó nincs a rácsban vagy már megtaláltad.")
            input("Nyomj Entert a folytatáshoz...")
            continue
        if guess in found_words:
            print("Ezt a szót már megtaláltad.")
            input("Nyomj Entert a folytatáshoz...")
            continue

        x, y, dx, dy = word_positions[guess]
        for i in range(len(guess)):
            found_positions.add((x + dx*i, y + dy*i))
        found_words.add(guess)
        print(f"Helyes! Megtaláltad: {guess}")
        input("Nyomj Entert a folytatáshoz...")

    clear_screen()
    print("Szókereső játék!")
    print_grid(grid, found_positions)
    print("\nJáték vége!")
    if len(found_words) == len(words):
        print("Gratulálok, mindent megtaláltál!")
    else:
        print("Legközelebb sikerül!")

if __name__ == "__main__":
    main()