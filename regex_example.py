import re
import unicodedata

var = "elemezzük ki ezt a mondatot ,Pythonban, pythonban"

m = re.match(r"(.*) ezt (.*)", var)

if m:
    print(m.group(1))
    print(m.group(2))

s = re.search(r"(pythonban)", var, re.IGNORECASE)

if s:
    print(s.group())

else:
    print("nincs találat")


email = "info@t_rossz_est.com"
m = re.search(r"_rossz_", email)

if m:
    print("megvan")
    print(m.start())
    print(m.end())
    print("email cím: ", email[: m.start()] + email[m.end():])
else:
    print("nincs meg")

telefon = "kerem hívja ezt a számot # +36-1/123-4567"
t_number = re.sub(r"\D", "", telefon)
print(t_number)

text = "árvíztűrő tükörfúrógép"
# text = re.sub(r+"[Áá]", "a", text)
nfd = unicodedata.normalize("NFD", text)
clean = re.sub(r"[\u0300-\u036f]", "", nfd)
print(clean)