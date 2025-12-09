import re

rendszamok = ["ABC-123", "ABCD-123", "AAAO-123", "XYZA-999", "AB-1234"]

for r in rendszamok:
    if re.match(r"^([A-Z]{3}-\d{3}|[A-Z]{4}-\d{3})$", r):
        print(r, "-> Érvényes")
    else:
        print(r, "-> Nem jó")