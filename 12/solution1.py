import numpy as np

startord = ord("S")
endord = ord("E")

grid = []
log = []

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		grid.append([ord(char) for char in line])

grid = np.array(grid)
shape = grid.shape

class path:
	def __init__(self, coords, nsteps=None):
		if nsteps is None:
			# copy
			self.coords = np.copy(coords.coords)
			self.nsteps = coords.nsteps
			self.log = coords.log.copy()
		else:
			# new path
			self.coords = coords
			self.nsteps = nsteps
			self.log = [self.coords]
	def do_step(self, dim, direction):
		self.coords[dim] += direction
		self.nsteps += 1
		self.log.append(self.coords)

def check_valid_move(cur_coords, move):
	new_coords = cur_coords + move
	if new_coords[0] >= 0 and new_coords[1] >= 0 and new_coords[0] <= shape[0] - 1 and new_coords[1] <= shape[1] - 1:
		newVal = grid[tuple(new_coords)]
		curVal = grid[tuple(cur_coords)]
		if newVal - 1 <= curVal:
			return True
	return False

def add_paths(x):
	newpaths = []
	cur_coords = x.coords
	if check_valid_move(cur_coords, [-1, 0]): # left
		newpath = path(x)
		newpath.do_step(0, -1)
		newpaths.append(newpath)
	if check_valid_move(cur_coords, [1, 0]): # right
		newpath = path(x)
		newpath.do_step(0, 1)
		newpaths.append(newpath)
	if check_valid_move(cur_coords, [0, 1]): # up
		newpath = path(x)
		newpath.do_step(1, 1)
		newpaths.append(newpath)
	if check_valid_move(cur_coords, [0, -1]): # down
		newpath = path(x)
		newpath.do_step(1, -1)
		newpaths.append(newpath)
	return newpaths

startpos = np.ravel(np.where(grid == startord))
endpos = np.ravel(np.where(grid == endord))
grid[tuple(startpos)] = ord("a")
grid[tuple(endpos)] = ord("z")
pathlist_check = [path(startpos, 0)]
path_done = None
iii = 0

while len(pathlist_check) > 0:
	iii += 1
	newpath_candidates = []
	for ipath in pathlist_check:
		print(ipath.coords)
		icandidates = add_paths(ipath)
		for jpath in icandidates:
			if np.all(jpath.coords == endpos):
				path_done = jpath
			elif (path_done is None) or (jpath.nsteps < path_done.nsteps):
				if not np.any([list(jpath.coords) == list(iipath) for iipath in log]):
					newpath_candidates.append(jpath)
					log.append(jpath.coords)
	pathlist_check = newpath_candidates

if path_done:
	print(path_done.nsteps)
	print(path_done.log)
else:
	print("nope")

print("done")