numbers = set()
while True:
    n = int(input("Wprowadź liczbę: "))
    if n in numbers:
        break
    numbers.add(n)
