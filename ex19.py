
divisible = []
for i in range(1000):
    if not i%6:
        divisible.append(i)
print(len(divisible))
print(divisible)

contains_7 = []
for n in divisible:
    if "7" in str(n):
        contains_7.append(n)
print(len(contains_7))
print(contains_7)
