#Day 5 assignment 1
def naughty():
	f = open('inputd51.txt', 'r')
	bad = ["ab","cd","pq","xy"]
	good = ['a','e','i','o','u']
	amount = 0
	for line in f:
		double = False
		g = True
		vowels = 0
		line = line.strip()
		if line[0] in good:
			vowels += 1
		for x in range(0, len(line)-1):
			first = line[x]
			second = line[x+1]
			combined = first + second
			if combined in bad:
				g = False
				break
			if first == second:
				double = True
			if second in good:
				vowels += 1
		if double and g and (vowels >= 3):
			amount += 1
	return amount

#Day 5 assignment 2
def nOrN():
	f = open('inputs/inputd52.txt', 'r')
	amount = 0
	for line in f:
		pairs = []
		letter = False
		double = False
		line = line.strip()
		l = len(line)
		for x in range (0, l-2):
			first = line[x]
			second = line[x+1]
			third = line[x+2]
			pairs.append([first+second, [x, x+1]])
			if first == third:
				letter = True
		pairs.append([line[l-2]+line[l-1],[l-2,l-1]])
		y = 1
		for pair in pairs:
			for x in range(y,len(pairs)):
				if pair[0] == pairs[x][0]:
					if not(pair[1][1] == pairs[x][1][0]):
						double = True
			y += 1
		if double and letter:
			amount += 1
	return amount
						
