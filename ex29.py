import random
import re
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

print(indexes)