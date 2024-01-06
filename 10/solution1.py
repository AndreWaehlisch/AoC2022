import numpy as np

X = 1
cycle = 0

results = []

def docycle():
	global cycle
	cycle += 1
	if (cycle - 20) % 40 == 0:
		results.append(cycle * X)

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		cmd, *par = line.split()
		if cmd == "noop":
			docycle()
		elif cmd == "addx":
			docycle()
			docycle()
			X += int(par[0])
	print(np.sum(results))
