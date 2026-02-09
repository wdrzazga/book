V1 = [1, 3, 5, 7, 9]
V2 = [1, 4, 7, 11, 15]
V3 = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 20]

common = []
for i in range(len(V1)):
    a = V1[i]
    if a in V2:
        common.append(a)

sum_1_2 = V1 + V2
result = []

V3copy = V3.copy()

for i in set(sum_1_2):
    if  i in V3:
        print("removing " + str(i))
        V3copy.remove(i)

print(common)
print(result)
print(V3copy)
print(ValueError)