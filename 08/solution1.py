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
	total = n * n
	visible = 4 * n - 4
	invisible = 0
	for i in range(1, n-1):
		for j in range(1, n-1):
			cur = arr[i,j]
			if np.any(np.less_equal(cur, arr[:i, j])) and np.any(np.less_equal(cur, arr[i+1:, j])) and np.any(np.less_equal(cur, arr[i, :j])) and np.any(np.less_equal(cur, arr[i, j+1:])):
				invisible += 1
				print("invis")
			else:
				visible += 1
				print("vis")
	print("total", total)
	print("sum", visible + invisible)
	print("vis", visible)
	print("invis", invisible)
