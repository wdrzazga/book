from random import randint

numbers = []

for i in range(1, 6):
    numbers.append(int(input(f"Podaj {i} liczbę: ")))

previous = -(10*100)
ascending = True
for n in numbers:
    if not n > previous:
        ascending = False
    previous = n
if ascending: print("Liczby są w kolejności rosnącej")
