var = input(" Írj be egy szöveget: ")
count = 0
for character in var:
    if character.lower() in "aáeéiíoóöőuúüű":
        count += 1
print("A szöveg hossza:", len(var))   #vagy print("A szöveg %s hosszu" %len(var))
print("A szövegben a magánhazók száma: ", count) #vagy print("A szövegben %s db magánhangzó van" %count)


