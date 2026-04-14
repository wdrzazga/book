symbols = list('xPQ4\n%u@eTB$!:"1<dkL$)$BxwqPcXB>?[rx$#}|dlnbV!')

appeared = []
repeated = set()
for i in range(1, len(symbols)-1):
	symbol = symbols[i]
	if symbol in appeared:
		repeated.add(symbol)
	else:
		appeared.append(symbol)

print(repeated)

digits = filter(lambda n: n.isdigit(), symbols)
sum = 0
for digit in digits:
	sum += int(digit)
print(sum)