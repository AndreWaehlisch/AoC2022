import numpy as np

result = 0
index = 1

def checkokay(a, b):
	if isinstance(a, int) and isinstance(b, int):
		if a > b:
			return -1
		elif a == b:
			return 0
		else:
			return 1
	elif isinstance(a, list) and isinstance(b, list):
		for i, j in zip(a, b):
			temp = checkokay(i, j)
			if temp == -1:
				return -1
			elif temp == 1:
				return 1
		if len(b) < len(a):
			return -1
		elif len(b) == len(a):
			return 0
		else:
			return 1
	elif isinstance(a, list):
		return checkokay(a, [b])
	elif isinstance(b, list):
		return checkokay([a], b)

def check_lines(lineA, lineB):
	global result, index
	alist = eval(lineA)
	blist = eval(lineB)
	if checkokay(alist, blist) == 1:
		result += index

with open("input", "r") as file:
	lineA = None
	for i, theline in enumerate(file):
		if lineA is None:
			lineA = theline.rstrip()
			if lineA == "":
				lineA = None
		else:
			lineB = theline.rstrip()
			check_lines(lineA, lineB)
			lineA = None
			index += 1

print(result)
