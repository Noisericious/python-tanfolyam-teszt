var = input("Írjon be egy szót: ")
if var.lower() == var[::-1].lower():
    print("A megadott szó palindrom.")
else:
    print("A megadott szó nem palindrom.")