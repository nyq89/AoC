
from collections import defaultdict
from itertools import permutations

#Day9 assignment 1 and 2
places = set()
graph = defaultdict(dict)

def sails():
	f = open('inputs/inputd91.txt', 'r')
	for line in f:
		(source, _, dest, _, distance) = line.strip().split()
		places.add(source)
		places.add(dest)
		graph[source][dest] = int(distance)
		graph[dest][source] = int(distance)

	distances = []

	for perm in permutations(places):
		distances.append(sum(map(lambda x,y: graph[x][y], perm[:-1], perm[1:])))

	print min(distances), max(distances)
