def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

szoveg = input("Adj meg egy szót: ")
if is_palindrome(szoveg):
    print(f"{szoveg} palindróm!")
else:
    print(f"{szoveg} nem palindróm!")