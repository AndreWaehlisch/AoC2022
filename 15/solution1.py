import numpy as np
from tqdm import tqdm
from numba import jit

result = 0
column = 10

with open("input", "r") as file:
	num_lines = sum(1 for line in file)

def distance(a, b):
	return sum(((abs(a[0] - b[0]), abs(a[1] - b[1]))))

with open("input", "r") as file:
	for i, theline in enumerate(tqdm(file, total=num_lines)):
		line = theline.rstrip()
		linesplit = line.split()
		sensor = int(linesplit[2][2:-1]), int(linesplit[3][2:-1])
		beacon = int(linesplit[8][2:-1]), int(linesplit[9][2:])
		curdist = distance(sensor, beacon)
		for j in range(int(-4E6), int(9E6)):
			jdist = distance(sensor, (j, column))
			if jdist <= curdist:
				result += 1
