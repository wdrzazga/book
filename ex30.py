import math

weight = 1

tgr = (1 + math.sqrt(5)) / 2 #the golden ratio
psi = (tgr - 1) * -1

print(tgr)
print(psi)

def fibonacci(n):
    return round((tgr**n - psi**n) / math.sqrt(5))

print(fibonacci(13))
