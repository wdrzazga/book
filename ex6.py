numbers = (input("Podaj liczby oddzielone spacją: ")).split(" ")

even = 0
odd = 0

for number in numbers:
    if int(number) % 2 == 0:
        even += 1
    else:
        odd += 1
print("Parzyste: ", even)
print("Nieparzyste: ", odd)
