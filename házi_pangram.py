import string
import unicodedata

def is_pangram(text: str) -> bool:
    alphabet = string.ascii_lowercase + "öüóőúűáéí"
    normalized = unicodedata.normalize("NFC", text).lower()
    letters_in_text = {char for char in normalized if char in alphabet}
    return letters_in_text.issuperset(alphabet)

print(is_pangram("Egy hűtlen vejét fülöncsípő, dühös mexikói úr Wesselényinél mázol Quitóban."))
print(is_pangram("nem az"))