import random


def get_word_list(difficulty: str):
    """
    The word list with the different difficulty levels
    :param difficulty: The difficulty level
    :return: The words
    """
    easy_words = ["cica", "apa", "anya", "baba", "nap"]
    medium_words = ["iskola", "abroncs", "mozdony", "bicikli", "telefon"]
    hard_words = ["pszichológia", "elegancia", "technológia", "fluxuskondenzátor", "környezetvédelem"]

    if difficulty == "easy":
        return easy_words
    elif difficulty == "medium":
        return medium_words
    return hard_words

def choose_difficulty() -> str:
    """
    Choose difficulty level
    :return: The chosen difficulty level
    """
    while True:
        diff = input("Choose difficulty level: (easy, medium, hard): ").lower()
        if diff in ["easy", "medium", "hard"]:
            return diff
        print("Érvénytelen választás, csak easy, medium vagy hard adható meg!")

def choose_word(word_list: list[str]) -> str:
    """
    Choose a random word from the word list
    :param word_list: The word list
    :return: The chosen word
    """
    return random.choice(word_list).upper()

def draw_hangman(tries_left: int):
    """
    Draw the hangman game
    :param tries_left: Tries left in number
    :return: The selectec "drawing"
    """
    stages = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
       =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\ |
             |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|\\ |
        /    |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|\\ |
        / \\ |
             |
        =========
        """
   ]
    print(stages[6 - tries_left])

def display_game_state(hidden_word: list[str], incorrect_guesses: list[str], tries_left: int):
    """
    Display the game state
    :param hidden_word: The hidden word
    :param incorrect_guesses: Incorrect guesses
    :param tries_left: Tries left from the game
    """
    draw_hangman(tries_left)
    print("\nJelenlegi állás: ")
    print(" ".join(hidden_word))
    print("Hibás próbálkozások száma: ", len(incorrect_guesses))
    print("Hibás próbálkozások: ", incorrect_guesses)
    print("Hátralévő próbálkozások száma: ", tries_left)

def get_player_guess(incorrect_guesses: list[str], correct_guesses: list[str]):
    while True:
        guess = input("Adj meg egy betűt: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Kérlek csak egy betűt adj meg")
        elif guess in incorrect_guesses or guess in correct_guesses:
            print("Ezt már próbáltad!")
        return guess

def update_hidden_words(word: str, hidden_word: list[str], guess: str):
    for i, char in enumerate(word):
        if char == guess:
            hidden_word[i] = guess

def is_game_lost(tries_left: int) -> bool:
    return tries_left <= 0

def is_game_won(hidden_word: list[str]) -> bool:
    return "_" not in hidden_word

def display_statistics(stats: dict):
    print("\nJáték statisztika")
    print(f"Az összes játék: {stats["total_games"]}")
    print(f"Győzelmek: {stats["games_won"]}")
    print(f"Helyesen kitalált szavak: {stats['words_guessed']}")
    print(f"Hátralévő probálkozások száma a győztes játékban: {stats['tries_remaining']}")

def update_statistics(stats: dict, won: bool, word: str, tries_left: int):
    stats["total_games"] += 1
    if won:
        stats["games_won"] += 1
        stats["words_guessed"].append(word)
        stats["tries_remaining"].append(tries_left)

def start():
    stats = {"total_games": 0, "games_won": 0, "words_guessed": [], "tries_remaining": []}
    print("Üdvözöljük, az akasztófa játékban!")
    while True:
        difficulty = choose_difficulty()
        word_list = get_word_list(difficulty)
        word = choose_word(word_list)
        hidden_word = ["_"] * len(word)
        incorrect_guesses = []
        correct_guesses = []
        tries_left = 6
        game_over = False

        while not game_over:
            display_game_state(hidden_word, incorrect_guesses, tries_left)
            guess = get_player_guess(incorrect_guesses, correct_guesses)

            if guess in word:
                correct_guesses.append(guess)
                update_hidden_words(word, hidden_word, guess)
                if is_game_won(hidden_word):
                    print(f"Gratulálunk, nyertél! A helyes szó a {word} volt!")
                    game_over = True
                    update_statistics(stats, won=True, word=word, tries_left=tries_left)

            else:
                incorrect_guesses.append(guess)
                tries_left -= 1
                if is_game_lost(tries_left):
                    draw_hangman(tries_left)
                    print(f"Sajnálom, de vesztettél! A szó a {word} volt!")
                    game_over = True
                    update_statistics(stats, won=False)
        display_statistics(stats)

        choice = input("Szeretnél új játékot? (Igen/Nem): ").lower().strip()
        if choice.startswith("n"):
            break

if __name__ == "__main__":
    start()



