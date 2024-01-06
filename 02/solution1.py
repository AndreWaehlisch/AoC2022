import numpy as np

results = [0]

baseScore = { "X" : 1, "Y" : 2, "Z" : 3}

def matchScore(i, j):
	if j == "X":
		if i == "A":
			return 3
		elif i == "B":
			return 0
		else:
			return 6
	elif j == "Y":
		if i == "A":
			return 6
		elif i == "B":
			return 3
		else:
			return 0
	else:
		if i == "A":
			return 0
		elif i == "B":
			return 6
		else:
			return 3

def getpoints(i, j):
	return baseScore[j] + matchScore(i, j)

score = 0
with open("input", "r") as file:
	for theline in file:
		line = theline.rstrip()
		i = line[0]
		j = line[-1]
		score += getpoints(i, j)

print(score)
