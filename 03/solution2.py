import numpy as np

def prio(item):
	if item.isupper():
		return ord(item) - 38
	else:
		return ord(item) - 96

assert prio("a") == 1
assert prio("A") == 27

assert prio("r") == 18
assert prio("Z") == 52

result = 0
with open("input", "r") as file:
	grouplist = []
	for i, theline in enumerate(file):
		line = theline.rstrip()
		grouplist.append(list(line))
		if ((i + 1) % 3) == 0:
			intersect1 = np.intersect1d(grouplist[0], grouplist[1])
			intersect2 = np.intersect1d(grouplist[0], grouplist[2])
			intersect3 = np.intersect1d(intersect1, intersect2)
			assert len(intersect3) == 1
			result += prio(intersect3[0])
			grouplist = []

print(result)
