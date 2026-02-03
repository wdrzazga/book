V = [1, 2, 4, 3, 6, 8, 7, 7, 8, 3, 4, 5, 6, 7, 1, 3, 9, 1, 0, 4, 2, 3, 6, 9]

sub_arrays = []

for i in range(len(V)-2):
    a = V[i]
    b = V[i+1]
    c = V[i+2]
    if a <= b <= c:
        sub_arrays.append(V[i:i+3])

print(sub_arrays)