#Day 3 assignment 1
def deliver():
	f = open('inputd31.txt', 'r')
	vert = 0
	horz = 0
	visits = []
	coord = (vert, horz)
	visits = put(coord, visits)
	for line in f:
		for c in line:
			if c=='^':
				horz += 1
				coord = (vert, horz)
				visits = put(coord, visits)
			elif c == 'v':
				horz -= 1
				coord = (vert, horz)
				visits = put(coord, visits)
			elif c == '<':
				vert -= 1
				coord = (vert, horz)
				visits = put(coord, visits)
			elif c == '>':
				vert += 1
				coord = (vert, horz)
				visits = put(coord, visits)
	print len(visits)

def put(co, li):
	for c in li:
		if co in c:
			c[1] = c[1] + 1
			return li
	li.append([co, 1])
	return li
		
#Day 3 assignment 2
def dub():
	f = open('inputd32.txt', 'r')
	vertS = 0
	horzS = 0
	vertE = 0
	horzE = 0
	visits = []
	coord = (vertS, horzS)
	visits = put(coord, visits)
	cord = (vertE, horzE)
	visits = put(coord, visits)
	sOrE = 0
	for line in f:
		for c in line:
			if c=='^':
				if (sOrE % 2) == 0:
					vertE += 1
					coord = (vertE, horzE)
				else:
					vertS += 1
					coord = (vertS, horzS)
				visits = put(coord, visits)
			elif c == 'v':
				if (sOrE % 2) == 0:
					vertE -= 1
					coord = (vertE, horzE)
				else:
					vertS -= 1
					coord = (vertS, horzS)
				visits = put(coord, visits)
			elif c == '<':
				if (sOrE % 2) == 0:
					horzE -= 1
					coord = (vertE, horzE)
				else:
					horzS -= 1
					coord = (vertS, horzS)
				visits = put(coord, visits)
			elif c == '>':
				if (sOrE % 2) == 0:
					horzE += 1
					coord = (vertE, horzE)
				else:
					horzS += 1
					coord = (vertS, horzS)
				visits = put(coord, visits)
			sOrE += 1
	print len(visits)

	
