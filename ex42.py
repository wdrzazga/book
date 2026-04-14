from random import choice

english_alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

tries = 0
while not False:
	letter = choice(english_alphabet)
	print(letter, end='')
	if letter in 'Az':
		print(f"\nZnaleziono litere {letter} po {str(tries)} próbach")
		break
	tries += 1
