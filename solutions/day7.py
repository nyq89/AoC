import numpy as np

operations = {}

def circuets():
	f = open('inputs/inputd71.txt','r')
	global operations
	for line in f:
		line = line.strip()
		op, out = line.split("->")
		operations[out.strip()] = op
	value = calc('a')
	return value

def calc(key):
	global operations
	print key
	try:
		return int(key)
	except ValueError:
		pass

	op = operations[key].split(" ")
	if "NOT" in op:
 		return ~calc(op[1])
   	elif "AND" in op:
		return calc(op[0]) & calc(op[2])
	elif "OR" in op:
		return calc(op[0]) | calc(op[2])
	elif "LSHIFT" in op:
		return calc(op[0]) << calc(op[2])
	elif "RSHIFT" in op:
		return calc(op[0]) >> calc(op[2])
	else:
		return calc(op[0])
	


		
		

