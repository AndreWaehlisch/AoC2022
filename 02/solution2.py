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

def decide_my_move(i, win_draw_lose):
	if win_draw_lose == "X": # lose
		if i == "A":
			return "Z"
		elif i == "B":
			return "X"
		else:
			return "Y"
	elif win_draw_lose == "Y": # draw
		if i == "A":
			return "X"
		elif i == "B":
			return "Y"
		else:
			return "Z"
	else: # win
		if i == "A":
			return "Y"
		elif i == "B":
			return "Z"
		else:
			return "X"

def getpoints(i, win_draw_lose):
	j = decide_my_move(i, win_draw_lose)
	return baseScore[j] + matchScore(i, j)

score = 0
with open("input", "r") as file:
	for theline in file:
		line = theline.rstrip()
		i = line[0]
		j = line[-1]
		score += getpoints(i, j)

print(score)
