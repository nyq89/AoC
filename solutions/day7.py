import operator
import numpy as np

#Day 7
ops = { None	:	lambda x : x,
		"NOT"	:	operator.invert,
		"AND"	:	operator.and_,
		"OR"	:	operator.or_,
		"RSHIFT":	operator.rshift,
		"LSHIFT":	operator.lshift }

gates = {}

class Gate:
	def __init__(self, op=None, *wires):
		self.op = op
		self.inw = [int(x) if x.isdigit() else x for x in wires]
		self.out = 0

	def cal_out(self):
		if not self.out:
			self.out = ops[self.op](*[np.uint16(x) if isinstance(x, int) else gates[x].cal_out() for x in self.inw])
		return self.out

def circuets():
	f = open('inputs/inputd71.txt','r')
	for line in f:
		op, out = line.split("->")
		op = op.split()
		out = out.strip()
		if len(op) == 1:
			gates[out] = Gate(None, op[0])
		else:
			gates[out] = Gate(op.pop(-2), *op)

	value = gates['a'].cal_out()
	return value

	
