import numpy as np
import re
from collections import defaultdict, deque

with open("input", "r") as file:
	lines = []
	for i, theline in enumerate(file):
		line = theline.rstrip()
		lines.append([int(height) for height in [*line]])

	arr = np.array(lines)
	n = len(lines)
	maxscore = 0
	for i in range(1, n-1):
		for j in range(1, n-1):
			cur = arr[i,j]
			scores = []
			try: # look up
				scores.append(np.where(np.greater_equal(np.flip(arr[:i, j] - cur), 0))[0][0] + 1)
			except IndexError:
				scores.append(len(arr[:i, j]))
			try: # look down
				scores.append(np.where(np.greater_equal(arr[i+1:, j] - cur, 0))[0][0] + 1)
			except IndexError:
				scores.append(len(arr[i+1:, j]))
			try: # right
				scores.append(np.where(np.greater_equal(arr[i, j+1:] - cur, 0))[0][0] + 1)
			except IndexError:
				scores.append(len(arr[i, j+1:]))
			try: # look left
				scores.append(np.where(np.greater_equal(np.flip(arr[i, :j] - cur), 0))[0][0] + 1)
			except IndexError:
				scores.append(len(arr[i, :j]))
			curscore = np.product(scores)
			if curscore > maxscore:
				maxscore = curscore
	print(maxscore)
