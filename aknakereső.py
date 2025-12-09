import os
import random

from dotenv import load_dotenv
from colorama import init, Fore, Style

load_dotenv()
init(autoreset=True)

COLOR_MAPPING = {
    "BLUE": Fore.BLUE,
    "GREEN": Fore.GREEN,
    "RED": Fore.RED,
    "MAGENTA": Fore.MAGENTA,
    "CYAN": Fore.CYAN,
    "YELLOW": Fore.YELLOW,
    "LIGHTRED_EX": Fore.LIGHTRED_EX,
    "LIGHTBLUE_EX": Fore.LIGHTBLUE_EX,
}

NUMBER_COLORS = {
    str(i): COLOR_MAPPING.get(os.getenv(f"COLOR_{i}")) for i in range(1, 9)
}

GRID_SIZE = int(os.getenv("GRID_SIZE", 8))
NUM_MINES = int(os.getenv("NUM_MINES", 10))
EMPTY_CELL = " "

def create_minefield(**kwargs):
    grid_size = kwargs.get("grid_size", GRID_SIZE)
    num_mines = kwargs.get("num_mines", NUM_MINES)

    grid = [[EMPTY_CELL for _ in range(grid_size)] for _ in range(grid_size)]
    mines = set()

    while len(mines) < num_mines:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        mines.add((row, col))

    for row, col in mines:
        grid[row][col] = "M"

    return grid, mines

def calculate_numbers(grid):
    """
    Kell egy lista az összes iránnyal. A lista elemei pozíciós paraméter párok, tuple párok(dr, dc)
    * "dr" => A sorban történő elmozdulás (delra row)
    * "dc" => Az oszlopban történő elmozdulás (delra column)

    [(-1, -1),  (-1, 0),   (-1, 1)
     (0, -1),   (0, 0),    (0, 1),
     (1, -1),   (1, 0),    (1, 1)]

     Racs (5x5)
     (1, 1), (1,2), (1,3)
     (2, 1), (2,2), (2,3)
     (3, 1), (3,2), (3,3)

     (row + dr, col +dc) #kiadja a vizsgált elemet = (2 + -1, 2 + -1) = (1, 1)

    :param grid:
    :return:
    """
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == "M":
                continue
            mine_counter = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and grid[r][c] == "M":
                    mine_counter += 1
            grid[row][col] = str(mine_counter) if mine_counter > 0 else EMPTY_CELL

def colorize(text, *args):
    return "".join(args) + text + " " + Style.RESET_ALL

def display_grid(visible_grid):
    print("\n    " + " ".join(str(i) for i in range(GRID_SIZE)))
    print("---" * GRID_SIZE)
    for idx, row in enumerate(visible_grid):
        print(f"{idx} | " + " ".join(
            colorize(cell, NUMBER_COLORS.get(cell, Fore.LIGHTCYAN_EX if cell == "F" else Fore.RED if cell == "M" else ""))
            for cell in row
        ))

def reveal_cell_with_recursion(grid, visible_grid, row, col):
    if visible_grid[row][col] != EMPTY_CELL:
        return False

    if grid[row][col] == "M":
        return True

    def flood_fill(r, c):
        if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            return
        if visible_grid[r][c] != EMPTY_CELL or visible_grid[r][c] == "M":
            return
        visible_grid[r][c] = grid[r][c]
        if grid[r][c] == EMPTY_CELL:
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]:
                flood_fill(r + dr, c + dc)
    flood_fill(row, col)
    return False

def reveal_cell(grid, visible_grid, row, col):
    if visible_grid[row][col] != EMPTY_CELL:
        return False

    if grid[row][col] == "M":
        return True

    if grid[row][col] == EMPTY_CELL:
        visible_grid[row][col] = "*"
    else:
        visible_grid[row][col] = grid[row][col]

    stack = [(row, col)]
    processed = set()
    while stack:
        r, c = stack.pop()
        if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            continue

        if (r, c) in processed:
            continue

        if visible_grid[r][c] not in [EMPTY_CELL, "*"] or grid[r][c] == "M":
            continue

        processed.add((r, c))
        if grid[r][c] == EMPTY_CELL:
            visible_grid[r][c] = "*"  # <- minden üres cellát láthatóvá teszünk
        else:
            visible_grid[r][c] = grid[r][c]
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]:
                rv, cv, = r + dr, c + dc
                if 0 <= rv < GRID_SIZE and 0 <= cv < GRID_SIZE:
                    if grid[rv][cv] == EMPTY_CELL and (rv, cv) not in processed:
                        stack.append((rv, cv))
                    elif grid[rv][cv] != "M" and (rv, cv) not in processed:
                        visible_grid[rv][cv] = grid[rv][cv]
    return False


def toggle_flag(visible_grid, row, col):
    if visible_grid[row][col] == EMPTY_CELL:
        visible_grid[row][col] = "F"
    elif visible_grid[row][col] == "F":
        visible_grid[row][col] = EMPTY_CELL


def play():
    grid, mines = create_minefield()
    calculate_numbers(grid)
    visible_grid = [[EMPTY_CELL for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    revealed_cells = 0
    total_cells = GRID_SIZE * GRID_SIZE - NUM_MINES
    flags_left = NUM_MINES

    while revealed_cells < total_cells:
        display_grid(visible_grid)
        print("\nÚtmutató a játékhoz:")
        print("- R <sor> <oszlop>: Mező feltárása R 3 4 => feltárjuk a 3. sor 4. oszlopát")
        print("- F <sor> <oszlop>: Mező zászlózása F 3 4 => zászló lerakása a 3. sor 4. oszlopán")
        print("Koordináták tartománya: 0-tól", GRID_SIZE -1, "-ig terjednek")
        print("A zászlókat a gyanús helyekre teheted.")
        print("Ha aknára lépsz a játék véget ér. Ha megvan minden akna, akkor is vége a játéknak.")

        command = input("Adj meg egy parancsot (pl.: R 3 4): ").strip().upper()
        parts = command.split()

        if len(parts) != 3 or parts[0] not in ["F", "R"]:
            print("Érvénytelen parancs! Használj R vagy F parancsot a megfelelő formátumban!")
            continue

        try:
            action, row, col = parts[0], int(parts[1]), int(parts[2])
        except ValueError:
            print("Érvénytelen parancs, használnod kell számokat a koordináták megadásához!")
            continue

        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            print("Érvénytelen koordináta")
            continue

        if action == "F":
            toggle_flag(visible_grid, row, col)
            flags_left = NUM_MINES - sum(row.count("F") for row in visible_grid)
            print("A megmaradt zászlók: ", flags_left)
        elif action == "R":
            hit_mine = reveal_cell(grid, visible_grid, row, col)
            if hit_mine:
                print("\n BUMMMM, aknára léptél!")
                for r, c in mines:
                    visible_grid[r][c] = "M"
                display_grid(visible_grid)
                print("Vége a játénak")
                return
        revealed_cells = sum(1 for row in range(GRID_SIZE) for col in range(GRID_SIZE) if visible_grid[row][col] not in [EMPTY_CELL, "F"])
    print("Gratulálunk, nyertél! Minden biztonságos cella feltárásra került!")
    display_grid(visible_grid)

if __name__ == "__main__":
    play()