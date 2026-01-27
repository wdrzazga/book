numbers = []


while True:
    number = int(input("Wpisz liczbę: "))
    if 1 <= number <= 10:
        print(sum(numbers))
        break
    else:
        double = number*2
        numbers.append(double)
        print(double)
