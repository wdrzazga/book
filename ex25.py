V = []

while True:
    V.append(int(input("Wprowadź pierwszą liczbę: ")))
    V.append(int(input("Wprowadź drugą liczbę: ")))
    product = V[-1] * V[-2]
    if product > 1000:
        break
    else:
        V.append(product)
print(V)