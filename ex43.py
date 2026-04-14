from random import randint

numbers = []
for i in range(20):
	index = randint(0, len(numbers))
	n = randint(0, 20)
	try:
		numbers[index]
		result = numbers.copy()
		result[index] = n
		for j in range(index+1, len(numbers)-1):
			result[j+1] = numbers[j]
		numbers = result
	except IndexError:
		numbers.append(n)
print(numbers) #TODO