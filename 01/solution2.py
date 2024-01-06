import numpy as np

results = [0]

with open("input", "r") as file:
	for line in file:
		x = line.rstrip()
		if x == "":
			results.append(0)
		else:
			results[-1] += int(x)

print(sum(np.sort(results)[-3:]))
