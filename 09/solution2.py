import numpy as np
import re
from collections import defaultdict, deque

rope = [(0, 0) for i in range(10)]

posis = defaultdict(int)
posis[rope[-1]] = 1

def plot(rope):
	for j in range(-17, 17):
		for i in range(-17, 17):
			test = [np.all(np.equal(irope, (i, j))) for irope in rope]
			if np.any(test):
				symbol = str(np.min(np.where(test)[0]))
				if symbol == "0":
					symbol = "H"
				elif symbol == "9":
					symbol = "T"
			elif (i == j == 0):
				symbol = "s"
			else:
				symbol = "."
			print(symbol, end="")
		print("\n", end="")

def domove(dim, direction, n):
	global rope, posis, j
	for i in range(int(n)):
		rope_new = np.copy(rope)
		# move head
		rope_new[0, dim] += direction
		for iknot in range(1, 10):
			dists = np.subtract(rope_new[iknot-1, :], rope_new[iknot, :])
			distance = np.linalg.norm(dists)
			if 2 < distance < 2.9:
				# diagonal step
				rope_new[iknot, :] += np.sign(dists)
			elif distance == 2:
				# straight step
				step_dim = np.argmax(np.abs(dists))
				rope_new[iknot, step_dim] += np.sign(dists[step_dim])
			rope = tuple([tuple(knot) for knot in rope_new])
			posis[rope[-1]] += 1

def translate_move(move, n):
	if move == "R":
		return 0, 1, n
	elif move == "L":
		return 0, -1, n
	elif move == "U":
		return 1, 1, n
	elif move == "D":
		return 1, -1, n

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		move, n = line.split()
		domove(*translate_move(move, n))
	print(len(posis))
