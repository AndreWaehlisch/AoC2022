import numpy as np

with open("input", "r") as file:
	result = 0
	for i, theline in enumerate(file):
		line = theline.rstrip()
		pair1, pair2 = line.split(",")
		p1_start, p1_end = [int(j) for j in pair1.split("-")]
		p2_start, p2_end = [int(j) for j in pair2.split("-")]
		if (p1_start >= p2_start) and (p1_end <= p2_end):
			result += 1
		elif (p2_start >= p1_start) and (p2_end <= p1_end):
			result += 1

print(result)
