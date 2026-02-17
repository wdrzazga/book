V1 = [1, 3, 5, 7, 9]
V2 = [1, 4, 7, 11, 15]
V3 = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 20]

arrays = (V1, V2, V3)

common = []
for i in range(len(V1)):
    a = V1[i]
    if a in V2:
        common.append(a)

sum_1_2 = V1 + V2

v3minusv1plusv2 = V3.copy()

for i in set(sum_1_2):
    if  i in V3:
        print("removing " + str(i))
        v3minusv1plusv2.remove(i)

sum_all = []

for arr in arrays:
    for i in arr:
        if not i in sum_all:
            sum_all.append(i)

print("COmmon part " , common)
print("v3 - (v1+v2) = ",v3minusv1plusv2)
print(sum_all)
