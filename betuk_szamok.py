var = input("Írj be valamit: ")

if var.isalpha():
    print("Ez csak betűkből áll.")
elif var.isnumeric():
    print("Ez csak számokból áll.")
else:
    print("Ez vegyes karakteres.")
