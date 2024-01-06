import numpy as np
import re
from collections import defaultdict, deque


with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()

for i in range(4, len(line) + 1):
	sub = line[i - 4 : i]
	u = np.unique(list(sub))
	if len(u) == 4:
		print(i)
		break
