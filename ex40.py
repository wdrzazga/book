name = input("Jak sie nazywasz?: ")

vowels = 0
for symbol in name:
	if symbol.lower() in 'aeiouy':
		vowels += 1
rev_name_array = list(name)
for i in range(vowels // 2):
	print(name)
	rev_name_array.reverse()
	print(''.join(rev_name_array))
if vowels % 2:
	print(name)