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
