import random

right_triangle = False
tries = 0
while not right_triangle:
    number1 = round(random.uniform(0.0, 100.0), 2)
    number2 = round(random.uniform(0.0, 100.0), 2)
    number3 = round(random.uniform(0.0, 100.0), 2)

    ab = [number1, number2, number3]

    c = max(ab)
    ab.remove(c)

    right_triangle = c ** 2 == ab[0] ** 2 + ab[1] ** 2
    tries += 1

print("Zajęło", tries, "prób, aby zdobyć trójkąt prostokątny")