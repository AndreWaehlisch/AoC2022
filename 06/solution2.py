import numpy as np
import re
from collections import defaultdict, deque


with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()

for i in range(14, len(line) + 1):
	sub = line[i - 14 : i]
	u = np.unique(list(sub))
	if len(u) == 14:
		print(i)
		break
