import random

numbers = []
for i in range(3):
	numbers.append(random.randint(1, 100))



def remove_biggest(list_):
	biggest = list_[0]
	for n in numbers:
		if n > biggest:
			biggest = n
	list_.remove(biggest)
	return list_


biggest = max(numbers)
remove_biggest(numbers)
for i in range(biggest):
	print(sum(numbers))