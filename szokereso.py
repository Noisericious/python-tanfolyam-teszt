# 1. szókészlet létrehozása
# 2. szórács létrehozása
# 3. Szavak elhelyezése
# 4. Üres cellák feltöltése
# 5. Számozott rács megjelenítése
# 6. Felhaszálói input (koordináták)
# 7. Ha megtalálta akkor a megtalalt betuk kiemelese, színezése
import random

from colorama import init, Fore, Style

init(autoreset=True)


def get_word_list() -> list[str]:
    """
    The game word list
    :return: A list with words
    """
    return ["PYTHON", "PROGRAM", "LOGIKA", "WEB", "LAPTOP", "SZINTAXIS", "ALMAFA"]

def creat_empty_grid(size=10):
    """
    Create empty grid

    Args:
        size (int): The size of the grid
    Returns:
        The empty grid
    """
    return [[" " for _ in range(size)] for _ in range(size)]

def place_words_in_grid(grid, word):
    """
    Places the words in a grid

    Args:
        grid (list): The grid to place words in
        word (str): The word to place

    """
    size = len(grid)
    directions = ["horizontal", "vertical", "diagonal"]
    placed = False
    while not placed:
        good_positions = True
        direction = random.choice(directions)
        start_row, start_col = random.randint(0, size -1), random.randint(0, size -1)

        if direction == "horizontal" and start_col + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row][start_col + i] == word[i] != " ":
                    good_positions = False
                    break
            if not good_positions:
                continue
            for i in range(len(word)):
                if grid[start_row][start_col + i] == " " and good_positions:
                    grid[start_row][start_col + i] = word[i]
                    placed = True
        elif direction == "vertical" and start_row + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row + i][start_col] != " ":
                    good_positions = False
                    break
            if not good_positions:
                continue
            for i in range(len(word)):
                if grid[start_row + i][start_col] == " " and good_positions:
                    grid[start_row + i][start_col] = word[i]
                    placed = True
        elif direction == "diagonal" and start_col + len(word) <= size and start_row + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row + i][start_col + i] == " ":
                    good_positions = False
                    break
            if not good_positions:
                continue
            if grid[start_row + i][start_col + i] == " " and good_positions:
                grid[start_row + i][start_col + i] = word[i]
                placed = True

def fill_empty_cells(grid):
    """
    Fill the empty cells in the grid

    Args:
        grid (list): The grid to fill
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == " ":
                grid[row][col] = chr(random.randint(65, 90))

def display_grid(grid):
    """
    Display the grid with coordinates

    Args:
        grid (list): The grid to display
    """
    print("\nJátékrács (sor és oszlopszámokkal)")
    header = "    " + " ".join(f"{i}" for i in range(len(grid)))
    print(header)
    print("    " + "--" * len(grid))
    for idx, row in enumerate(grid):
        print(f"{idx} | " + " ".join(f"{Fore.GREEN}{cell}{Style.RESET_ALL}"
                                     if cell.islower() else cell for cell in row))

def get_number_input(user_str, size):
    """
    Handle user input and validate input

    Args:
        user_str(str): The user input
        size(int): The size of the grid

    Returns:
        The choose coordinate
    """
    while True:
        input_str = input(user_str)
        if input_str.isdigit() and 0<= int(input_str) < size:
            return int(input_str)


def get_word_selection(grid):
    """
    Get word selection

    Args:
         grid (list): The grid
    Returns:
        Coordinates
    """
    print("\nSegítség a koordináták megadásához:")
    print(" - Sor és oszlop számok adjon meg (pl.: kezdő sor: 2, oszlop: 3)")
    print(" - Végpontként adja meg a koordinátákat (pl: végsor: 2, oszlop: 7)")
    print("Példa a SZINTAXIS szóhoz a kezdő koordináta a (1,1), vég koordináta (1,8)")
    size = len(grid)
    start_row = get_number_input(f"Adja meg a szó kezdősorának számát(0-{size-1}): ", size)
    start_col = get_number_input(f"Adja meg a szó kezdőoszlopának számát(0-{size-1}): ", size)
    end_row = get_number_input(f"Adja meg a szó végsorának számát(0-{size-1}): ", size)
    end_col = get_number_input(f"Adja meg a szó végoszlopának számát(0-{size-1}): ", size)

    return start_row, start_col, end_row, end_col

def check_and_mark_word_in_grid(grid, word, start_row, start_col, end_row, end_col):
    """
    Check and mark a given word in the grid

    Args:
        grid (list): The grid
        word (str): The word to mark
        start_row (int): The starting row coordinate
        start_col (int): The starting column coordinate
        end_row (int): The ending row coordinate
        end_col (int): The ending column coordinate
    Returns:
        (boolean): Found
    """
    word_length = len(word)
    # vizszintes
    if start_row == end_row:
        if abs(start_col - end_col) + 1 == word_length:
             for i in range(word_length):
                 if grid[start_row][start_col + i] != word[i]:
                     return False
             for i in range(word_length):
                 grid[start_row][start_col + i] = grid[start_row][start_col + i].lower()
             return True
    # fuggőleges
    elif start_col == end_col:
        if abs(start_row - end_row) + 1 == word_length:
            for i in range(word_length):
                if grid[start_row + i][start_col] != word[i]:
                    return False
            for i in range(word_length):
                grid[start_row + i][start_col] = grid[start_row + i][start_col].lower()
            return True
    #átlós
    elif abs(start_row - end_row) + 1 == word_length and abs(start_col - end_col) + 1 == word_length:
        for i in range(word_length):
            if grid[start_row + i][start_col +i] != word[i]:
                return False
        for i in range(word_length):
            grid[start_row + i][start_col +i] = grid[start_row + i][start_col +i].lower()
        return True
    return False

def main():
    grid = creat_empty_grid()
    word_list = get_word_list()

    for word in word_list:
        place_words_in_grid(grid, word)

    fill_empty_cells(grid)
    display_grid(grid)

    print("\nRejtett szavak: ", ", ".join(word_list))

    found_words = []

    while len(found_words) < len(word_list):
        print("\nTalált szavak: ", ", ".join(found_words))
        selection = get_word_selection(grid)

        start_row, start_col, end_row, end_col = selection
        found = False
        for word in word_list:
            if word not in found_words and check_and_mark_word_in_grid(grid, word, start_row, start_col, end_row, end_col):
                print(f"Megtaláltad a szót: {word}")
                found_words.append(word)
                found = True
                break

        if not found:
            print("Nincs a megadott szavak között!")

        display_grid(grid)
    print("Gratulálunk, megtaláltad az összes szót!")

if __name__ == "__main__":
    main()


