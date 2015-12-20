import md5

#Day 4 assignment 1 and 2
def zeroes(code, zer):
	value = code
	x = 0
	finish = False
	while(True):
		solved = str(md5.new(value+ str(x)).hexdigest())
		for y in range(0,zer):
			if solved[y] != '0':
				finish = False
				break
			finish = True
		if finish:
			print solved
			print str(x)
			return
		x += 1
		if (x%1000) == 0:
			print x


	
