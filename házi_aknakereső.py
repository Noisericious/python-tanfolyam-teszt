import random
from colorama import Fore, Style, init
init(autoreset=True)

rows = 9
columns = 9
mine = 10

def new_game():
    """Makes a new game."""
    board = [[' ' for _ in range(columns)] for _ in range(rows)]
    mines = [[False for _ in range(columns)] for _ in range(rows)]
    revealed = [[False for _ in range(columns)] for _ in range(rows)]
    flagged = [[False for _ in range(columns)] for _ in range(rows)]
    return board, mines, revealed, flagged


def place_mines(mines):
    """Randomly places mines."""
    placed = 0
    while placed < mine:
        r = random.randint(0, rows - 1)
        c = random.randint(0, columns - 1)
        if not mines[r][c]:
            mines[r][c] = True
            placed += 1


def count_adjacent_mines(mines, r, c):
    """Counts the number of adjacent mines."""
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < columns and mines[nr][nc]:
                count += 1
    return count


def reveal_cell(board, mines, revealed, flagged, r, c):
    """Reveals a cell. If there are 0 mines next to it, it expands recursively."""
    if revealed[r][c] or flagged[r][c]:
        return False

    revealed[r][c] = True

    if mines[r][c]:
        board[r][c] = '*'
        print("\nBumm! Ráléptél egy aknára! Játék vége.\n")
        show_all(board, mines, revealed)
        return True

    adjacent = count_adjacent_mines(mines, r, c)
    board[r][c] = str(adjacent) if adjacent > 0 else ' '

    if adjacent == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns:
                    reveal_cell(board, mines, revealed, flagged, nr, nc)
    return False


def flag_cell(board, flagged, revealed, r, c):
    """Flags a cell, or removes the flag from a cell."""
    if revealed[r][c]:
        return
    flagged[r][c] = not flagged[r][c]
    board[r][c] = 'F' if flagged[r][c] else ' '


def print_board(board, revealed, flagged):
    """Prints the board."""
    print("\n   " + " ".join(str(c) for c in range(columns)))
    print("  +" + "--" * columns + "+")
    for r in range(rows):
        row_str = f"{r} |"
        for c in range(columns):
            if revealed[r][c]:
                row_str += board[r][c] + " "
            elif flagged[r][c]:
                row_str += Fore.BLUE + 'F' + Style.RESET_ALL + " "
            else:
                row_str += ". "
        print(row_str + "|")
    print("  +" + "--" * columns + "+")


def check_win(mines, revealed):
    """Checks if the board is win."""
    for r in range(rows):
        for c in range(columns):
            if not mines[r][c] and not revealed[r][c]:
                return False
    return True


def show_all(board, mines, revealed):
    """Reveals the board and prints the board after the game."""
    for r in range(rows):
        for c in range(columns):
            if mines[r][c]:
                board[r][c] = '*'
            elif not revealed[r][c]:
                adj = count_adjacent_mines(mines, r, c)
                board[r][c] = str(adj) if adj > 0 else ' '
    print_board(board, [[True] * columns for _ in range(rows)], [[False] * columns for _ in range(rows)])


def main():
    while True:
        board, mines, revealed, flagged = new_game()
        place_mines(mines)

        while True:
            print_board(board, revealed, flagged)
            command = input("Add meg a parancsot (reveal r c / flag r c): ").split()

            if len(command) != 3:
                print("Hibás formátum! Példa: reveal 2 3")
                continue

            action, r_str, c_str = command
            if not (r_str.isdigit() and c_str.isdigit()):
                print("A sor és oszlop legyen szám!")
                continue

            r, c = int(r_str), int(c_str)
            if not (0 <= r < rows and 0 <= c < columns):
                print("Érvénytelen koordináta.")
                continue

            if action == "reveal":
                lost = reveal_cell(board, mines, revealed, flagged, r, c)
                if lost:
                    break
            elif action == "flag":
                flag_cell(board, flagged, revealed, r, c)
            else:
                print("Ismeretlen parancs.")

            if check_win(mines, revealed):
                show_all(board, mines, revealed)
                print("\nGratulálok, minden aknát megtaláltál!\n")
                break


        choice = input("Szeretnél új játékot kezdeni? (y/n): ").lower().strip()
        if choice != "y":
            print("Kilépés. Köszönöm a játékot!")
            break


if __name__ == "__main__":
    main()