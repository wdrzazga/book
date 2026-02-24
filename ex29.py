import random
import re
from array import array

random.seed(random.randint(1, 2))

days = []


for i in range(365):
    days.append(random.randint(0, 1))

#days = [0,1,0,1,1,0,1,1,1]

print(days.count(1))
success_days = [d for d in days if d == 1]

print(len(success_days))

days_str = ""
for i in days:
    days_str += str(i)
matches = re.finditer(r'(1)+', days_str)

indexes = [(match.start(), match.end() - 1) for match in matches]
longest = [-1, 0]
for match in indexes:
    length = (match[1] - match[0]) + 1
    if length > longest[1]:
        longest[0] = match[0]
        longest[1] = length
print(longest)

indexes_filtered = [item for item in indexes if item[1] - item[0] > 5]
longest = [-1, (0, 0)]
for arr in indexes_filtered:
    arr_length = arr[1] - arr[0]
    if arr_length > longest[0]:
        longest[0] = arr_length
        longest[1] = arr

print(indexes)
print(indexes_filtered)
print(longest)