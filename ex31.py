numbers = [i+1 for i in range(200)]
print(sum([121, 122, 123, 124, 125, 126]))

def f(n):
    return (n+1) + (n+2) + (n+3) + (n+4) + (n+5) + (n+6)

def six_followers(n):
    return [(n+1), (n+2), (n+3), (n+4), (n+5), (n+6)]

amount = 0
for i in range(len(numbers)):
    result = f(numbers[i])
    if 1000 > result > 800:
        amount += 1
        print(six_followers(i))
print(amount)