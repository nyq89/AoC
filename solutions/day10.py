from itertools import groupby


def las(inp):
	s = ""
	for k, g in groupby(inp):
		s += str(len(list(g))) + str(k)
	return s

def loop_las(inp, loops):
	for _ in range(loops):
		inp = las(inp)
	print len(inp)
	
