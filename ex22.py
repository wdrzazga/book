numbers = []
previous = None
while True:
    n = int(input("Wprowadź liczbę: "))
    numbers.append(n)
    if previous == n:
        break
    else:
        previous = n