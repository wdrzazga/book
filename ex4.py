import re

vowels_in_word = []
consonants_in_word = []
digits_in_word = []

word = input("Wpisz coś: ")
vowels = re.findall('[aeiouy]', word)
consonants = re.findall('[bcdfghjklmnpqrstvwxz]', word)
digits = re.findall('[0-9]', word)

print("W podanym słowie znajduje się: ", len(vowels), "samogłosek")
print("W podanym słowie znajduje się: ", len(consonants), "spółgłosek")
print("W podanym słowie znajduje się: ", len(digits), "cyfr")
