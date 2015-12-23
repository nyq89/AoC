import numpy as np

def circuets():
	f = open('inputs/inputd71.txt','r')
	operations = []
	outputs = {}
	for line in f:
		line = line.strip()
		op, out = line.split("->")
		out = out.strip()
		if(op.strip().isdigit()):
			value = np.uint16(op.strip())
			outputs[out] = value
		else:
			outputs[out] = None
			operations.append([op.strip(), out])
	outputs = calc(outputs, operations)
	for key, value in outputs.iteritems():
		if not(value==None):
			print key, value
	return outputs.get('a')
		
def calc(out, op):
	if not(op):
		return(out)
	for operation in op:
		data = operation[0].split(" ")
		if 'AND' in data:
			if data[0].isdigit():
				val1 = np.uint16(data[0])
			else:
				val1 = out.get(data[0])
			if data[2].isdigit():
				val2 = np.uint16(data[2])
			else:
				val2 = out.get(data[2])
			if not(val1 == None) and not(val2 == None):
				value = val1 & val2
				print value, data, operation[1]
				out[operation[1]] = value
				op.remove(operation)
				out = calc(out,op)
				break
		elif 'OR' in data:
			if data[0].isdigit():
				val1 = np.uint16(data[0])
			else:
				val1 = out.get(data[0])
			if data[2].isdigit():
				val2 = np.uint16(data[2])
			else:
				val2 = out.get(data[2])
			if not(val1 == None) and not(val2 == None):
				value = val1 | val2
				print value, data, operation[1]
				out[operation[1]] = value
				op.remove(operation)
				out = calc(out,op)
				break
		elif 'RSHIFT' in data:
			if data[0].isdigit():
				val = np.uint16(data[0])
			else:
				val = out.get(data[0])
			if not (val==None):
				value = val >> int(data[2])
				print value, data, operation[1]
				out[operation[1]] = value
				op.remove(operation)
				out = calc(out,op)
				break
		elif 'LSHIFT' in data:
			if data[0].isdigit():
				val = np.uint16(data[0])
			else:
				val = out.get(data[0])
			if not (val==None):
				value = val << int(data[2])
				print value, data, operation[1]
				out[operation[1]] = value
				op.remove(operation)
				out = calc(out,op)
				break
		elif 'NOT' in data:
			if data[0].isdigit():
				val = np.uint16(data[0])
			else:
				val = out.get(data[0])
			if not (val==None):
				value = ~val
				print value, data, operation[1]
				out[operation[1]] = value
				op.remove(operation)
				out = calc(out,op)
				break
		else:
			if data[0].isdigit():
				value = np.uint16(data[0])
			else:
				value = out.get(data[0])
			if not (value==None):
				print value, data, operation[1]
				out[operation[1]] = value
				op.remove(operation)
				out = calc(out,op)
				break
	return out


		
		

