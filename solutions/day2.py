#Day 2 assignment 1
def package():
	f = open ('input21.txt', 'r')
	paper = 0
	for line in f:
		line = line.strip()
		mes = line.split('x')
		total = 2 * int(mes[0]) * int(mes[1]) + 2 * int(mes[2]) * int(mes[1]) +2 * int(mes[0]) * int(mes[2])
		paper += total
		mes = [ int(x) for x in mes]
		mes.sort()
		mini = int(mes[0]) * int(mes[1])
		paper += mini
		print mes
	print paper
#Day 2 assignment 2
def ribbon():
	f = open ('input22.txt', 'r')
	rib = 0
	for line in f:
		line = line.strip()
		mes = line.split('x')
		mes = [ int(x) for x in mes]
		mes.sort()
		print mes
		packrib = 2 * mes[0] + 2* mes[1]
		rib += packrib
		product = 1
		for x in mes:
			product *= x
		rib += product
	print rib
