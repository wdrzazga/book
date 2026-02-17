digits = []

while len(digits) < 5:
    symbol = input("Znak: ")[0]
    try:
        int(symbol)
        if symbol == '0' and len(digits) == 0:
            continue
        digits.append(symbol)
    except ValueError:
        pass

a = int("".join(digits))
print(a)
digits.reverse()
b = int("".join(digits))
print(b)
print(a + b)