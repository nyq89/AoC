#Day 6 assignment 1
def lightsComp():
	f = open('inputs/inputd61.txt', 'r')
	lights = [[False for x in range(1000)] for x in range(1000)]
	amount = 0
	for line in f:
		line = line.strip()
		data = line.split(" ")
		data.remove("through")
		if "turn" in data:
			data.remove("turn")
		l = len(data)
		if data[0] == "toggle":
			ligths = toggle(lights, data[l-2], data[l-1])
		if data[0] == "on":
			ligths = on(lights, data[l-2], data[l-1])
		if data[0] == "off":
			ligths = off(lights, data[l-2], data[l-1])
	for x in lights:
		for y in x:
			if y:
				amount += 1
	return amount
		
		

def toggle(lights, start, stop):
	sta = start.split(",")
	sto = stop.split(",")
	for x in range(int(sta[0]), int(sto[0])+1):
		for y in range(int(sta[1]),int(sto[1])+1):
			lights[x][y] = not(lights[x][y])
	return lights

def off(lights, start, stop):
	sta = start.split(",")
	sto = stop.split(",")
	for x in range(int(sta[0]), int(sto[0])+1):
		for y in range(int(sta[1]),int(sto[1])+1):
			lights[x][y] =  False
	return lights

def on(lights, start, stop):
	sta = start.split(",")
	sto = stop.split(",")
	for x in range(int(sta[0]), int(sto[0])+1):
		for y in range(int(sta[1]),int(sto[1])+1):
			lights[x][y] = True
	return lights


#Day 6 assignment 2
def lightsCount():
	f = open('inputs/inputd61.txt', 'r')
	lights = [[0 for x in range(1000)] for x in range(1000)]
	amount = 0
	for line in f:
		line = line.strip()
		data = line.split(" ")
		data.remove("through")
		if "turn" in data:
			data.remove("turn")
		l = len(data)
		if data[0] == "toggle":
			ligths = toggle(lights, data[l-2], data[l-1])
		if data[0] == "on":
			ligths = on(lights, data[l-2], data[l-1])
		if data[0] == "off":
			ligths = off(lights, data[l-2], data[l-1])
	for x in lights:
		for y in x:
			amount += y
	return amount
		
		

def toggle(lights, start, stop):
	sta = start.split(",")
	sto = stop.split(",")
	for x in range(int(sta[0]), int(sto[0])+1):
		for y in range(int(sta[1]),int(sto[1])+1):
			lights[x][y] += 2
	return lights

def off(lights, start, stop):
	sta = start.split(",")
	sto = stop.split(",")
	for x in range(int(sta[0]), int(sto[0])+1):
		for y in range(int(sta[1]),int(sto[1])+1):
			if lights[x][y] > 0:
				lights[x][y] -= 1
	return lights

def on(lights, start, stop):
	sta = start.split(",")
	sto = stop.split(",")
	for x in range(int(sta[0]), int(sto[0])+1):
		for y in range(int(sta[1]),int(sto[1])+1):
			lights[x][y] += 1
	return lights


