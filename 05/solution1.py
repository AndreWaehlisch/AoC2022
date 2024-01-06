import numpy as np
import re
from collections import defaultdict, deque

clist = defaultdict(deque)
moves = []
reading_cs = True
result = ""

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		if line == "":
			reading_cs = False
			continue
		elif reading_cs:
			m = np.array([x.start() for x in re.finditer("[A-Z]", line)])
			c_idx = m // 4 + 1
			c_name = [line[idx] for idx in m]
			for c_i, c_m in zip(c_idx, c_name):
				clist[c_i].append(c_m)
		else:
			moves.append((line.split()[1::2]))
	for num, source, target in moves:
		for imove in range(int(num)):
			item = clist[int(source)].popleft()
			clist[int(target)].appendleft(item)
	for c_i in range(len(clist)):
		result = result + clist[c_i + 1][0]
	print(result)
