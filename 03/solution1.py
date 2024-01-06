import numpy as np

def prio(item):
	if item.isupper():
		return ord(item) - 38
	else:
		return ord(item) - 96

assert prio("a") == 1
assert prio("A") == 27

result = 0
with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		part1 = list(line[:len(line)//2])
		part2 = list(line[len(line)//2:])
		intersect = np.intersect1d(part1, part2)
		assert len(intersect) == 1
		result += prio(intersect[0])

print(result)
