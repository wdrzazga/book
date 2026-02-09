from operator import indexOf

V = [1, 2, 4, 3, 6, 8, 7, 7, 8, 3, 4, 5, 6, 7, 1, 3, 9, 1, 0, 4, 2, 3, 6, 9]

sub_arrays = []

for i in range(len(V)-2):
    a = V[i]
    b = V[i+1]
    c = V[i+2]
    if a <= b <= c:
        sub_arrays.append(V[i:i+3])

lengths = []
for i in range(len(V)):
    number = V[i]
    index = i
    length = 1
    while True:
        if index != len(V)-1:
            next_elem = V[index + 1]
            if number <= next_elem:
                index += 1
                number = next_elem
                length += 1
            else:
                lengths.append(length)
                break
        else:
            lengths.append(length)
            break

numbers_occurrence = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

for i in range(len(V)):
    number = V[i]
    numbers_occurrence[number] += 1

print(numbers_occurrence)
biggest = max(lengths)
biggest_index = indexOf(lengths, biggest)
print(lengths[biggest_index:biggest_index+biggest])
print(sub_arrays)
