import numpy as np

X = 1
cycle = 0

def docycle():
	global cycle
	pixel = cycle % 40
	cycle += 1
	if abs(pixel - X) < 2:
		print("#", end="")
	else:
		print(".", end="")
	if pixel == 39:
		print("\n", end="")

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
