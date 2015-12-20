#Day 1 assignment 2
def floor():
	f = open('input12.txt', 'r')
	flo = 0
	pos = 0
	for line in f:
		for c in line:
			if c == '(':
				flo += 1
				pos += 1
			if c == ')':
				flo -= 1
				pos += 1
			if flo == -1:
				print pos
				return

