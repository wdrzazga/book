import random


numbers = []

for i in range(10):
    numbers.append(random.randint(1, 1000))
print(numbers)

first = []
second = []

for i in numbers:
    if not i%2: first.append(i)
    else: second.append(i)

sorted_numbers = first + second
print(sorted_numbers)
