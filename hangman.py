import random
import sys
import os

hangman_pics = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]


word_list = [
    "KISVONAT", "BITUMEN", "OKOSTOJAS", "VAKOLAT", "TESTEDZÉS", "PATYOLAT", "TENGER", "KARACSONY",
    "PROGRAM", "PYTHON", "FLUXUSKONDENZATOR", "HARMONIKA", "SZAMAR", "ELECTRIC"
]


def choose_word(random_mode=True):
    """You can choose a mode, single or multiplayer"""
    if random_mode:
        return random.choice(word_list).upper()

    else:
        print("Add meg a titkos szót (a másik játékos ne nézze!):")
        word = input(">>> ").strip().upper()

        while not word:
            print("A szó nem lehet üres!")
            word = input(">>> ").strip().upper()

        clear_screen()
        print("A szó elmentve, kezdődhet a játék!\n")
        return word


def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_state(missed, correct, secret):
    """Shows the state of the game"""
    print(hangman_pics[len(missed)])
    print("\nHibás tippek: ", " ".join(missed) if missed else "(nincs)")
    shown = []
    for ch in secret:
        if ch == " ":
            shown.append(" ")
        elif ch in correct:
            shown.append(ch)
        else:
            shown.append("_")
    print("\nSzó: " + " ".join(shown))
    print()


def input_guess(already_guessed):
    """Asks the user to guess a word"""
    while True:
        guess = input("Tippelj (egy betűt vagy az egész szót): ").strip().upper()
        if not guess:
            print("Adj meg valamit.")
            continue
        if len(guess) == 1:
            if not guess.isalpha():
                print("Kérlek csak betűt írj be.")
                continue
            if guess in already_guessed:
                print("Ezt a betűt már próbáltad.")
                continue
            return guess
        else:
            return guess

def play_one_game(secret):
    """Conducts one game of Hangman, returns True if won, False is lost."""
    missed = []
    correct = set()
    all_guessed = set()

    max_wrong = len(hangman_pics) - 1

    while True:
        clear_screen()
        display_state(missed, correct, secret)

        all_letters_in_secret = set([ch for ch in secret if ch != " "])
        if all_letters_in_secret.issubset(correct):
            print("Gratulálok — nyertél! A szó:", secret)
            return True

        if len(missed) >= max_wrong:
            clear_screen()
            display_state(missed, correct, secret)
            print("Vesztettél — elfogyott a próbálkozásod. A szó:", secret)
            return False

        guess = input_guess(all_guessed)
        clear_screen()
        if len(guess) > 1:
            if guess == secret:
                print("Bravó! Teljes szóval eltaláltad.")
                return True
            else:
                print("Nem jó teljes szó.")
                missed.append(guess)
                all_guessed.add(guess)
                continue

        all_guessed.add(guess)
        if guess in secret:
            correct.add(guess)
            print(f"Talált! A '{guess}' benne van a szóban.")

        else:
            missed.append(guess)
            print(f"Nincs benne: '{guess}'.")


def main():
    clear_screen()
    print("=== Akasztófa játék ===")
    while True:
        mode = ""
        while mode not in ("1", "2"):
            print("\nVálassz módot:")
            print(" 1) Véletlenszerű szó")
            print(" 2) Kétszemélyes mód (valaki beírja a titkos szót)")
            mode = input("Melyik? (1/2): ").strip()

        if mode == "1":
            secret = choose_word(random_mode=True)
        else:
            secret = choose_word(random_mode=False)

        result = play_one_game(secret)

        again = input("\nSzeretnél új játékot? (i/n): ").strip().lower()
        if not again or again[0] != "i":
            print("Köszi a játékot — viszlát!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKilépés. Viszlát!")
        sys.exit(0)