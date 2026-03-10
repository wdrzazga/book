L = [i for i in range(30)]

groups_3 = []

for i in range(5, 30):
    groups_3.append((i-4, i-2, i))
print("Co 3:\n")
for group in groups_3:
    if sum(group) % 5 == 0:
        print(group)

groups_2 = []

for i in range(7, 30):
    groups_2.append((i-6, i-3, i))

print("Co 2:\n")
for group in groups_2:
    if sum(group) % 5 == 0:
        print(group)