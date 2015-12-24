import re

#Day 8 assignment 1
def num_chars():
	f = open('inputs/inputd81.txt', 'r')
	amount = 0
	for line in f:
		line = line.strip()
		amount += len(line) - len(eval(line))
	return amount

#Day 8 assignment 2
def num_chars2():
	f = open('inputs/inputd81.txt', 'r')
	amount = 0
	for line in f:
		line = line.strip()
		amount += len(re.escape(line)) + 2 - len(line)
	return amount
