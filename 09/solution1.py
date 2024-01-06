import numpy as np
import re
from collections import defaultdict, deque

H_coords = (0, 0)
T_coords = (0, 0)

posis = defaultdict(int)
posis[T_coords] = 1

def domove(dim, direction, n):
	global H_coords, T_coords, posis
	for i in range(int(n)):
		H_coords_new = np.copy(H_coords)
		T_coords_new = np.copy(T_coords)
		# move head
		H_coords_new[dim] += direction
		dists = np.subtract(H_coords_new, T_coords_new)
		distance = np.linalg.norm(dists)
		if 2 < distance < 2.3:
			# diagonal step
			T_coords_new += np.sign(dists)
		elif distance == 2:
			# straight step
			step_dim = np.argmax(np.abs(dists))
			T_coords_new[step_dim] += np.sign(dists[step_dim])
		H_coords = tuple(H_coords_new)
		T_coords = tuple(T_coords_new)
		posis[T_coords] += 1

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
