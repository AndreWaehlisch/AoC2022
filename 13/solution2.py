import numpy as np
from functools import cmp_to_key

result = 0

def checkokay(a, b):
	if isinstance(a, int) and isinstance(b, int):
		if a > b:
			return 1
		elif a == b:
			return 0
		else:
			return -1
	elif isinstance(a, list) and isinstance(b, list):
		for i, j in zip(a, b):
			temp = checkokay(i, j)
			if temp == -1:
				return -1
			elif temp == 1:
				return 1
		if len(b) < len(a):
			return 1
		elif len(b) == len(a):
			return 0
		else:
			return -1
	elif isinstance(a, list):
		return checkokay(a, [b])
	elif isinstance(b, list):
		return checkokay([a], b)

lines = [[2], [6]]
with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		if line != "":
			lines.append(eval(line))
	lines.sort(key=cmp_to_key(checkokay))

packet1 = lines.index([2]) + 1
packet2 = lines.index([6]) + 1

print(packet1 * packet2)
