letters = []
vowels = "aeouiy"
remaining = []

while True:
    char = input("Wpisz literę: ")
    if len(char) > 1:
        print("Nie")
    elif char in vowels:
        letters.append(char)
    elif char == "*":
        letters.pop(0)
    elif char == "#":
        if len(remaining) > 0:
            remaining.pop()
        else:
            letters.pop()
    elif char == "!":
        print(letters + remaining)
        break
    else:
        remaining.append(char)
