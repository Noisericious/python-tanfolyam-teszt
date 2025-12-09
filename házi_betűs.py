import unicodedata

def count_small_and_upper_letters(s: str) -> None:
    d = {"upper": 0, "lower": 0}
    for char in s:
        if char.isupper():
            d["upper"] += 1
        elif char.islower():
            d["lower"] += 1
    print("Az eredeti szöveg: " + s)
    print("A nagybetűk száma a szövegben: ", d["upper"])
    print("A kisbetűk száma a szövegben: ", d["lower"])

count_small_and_upper_letters("ASDaS aSd saD asD af")

def count_small_and_upper_letters2(s: str) -> dict:
    s_norm = unicodedata.normalize("NFC", s)
    upper = sum(1 for char in s_norm if char.isupper())
    lower = sum(1 for char in s_norm if char.islower())

    return {
        "original": s,
        "normalized": s_norm,
        "upper": upper,
        "lower": lower,
    }

print(count_small_and_upper_letters2("Ólajtó"))