import numpy as np

#  0 = air
#  1 = sand
# -1 = rock

result = 0

offset = 4000
n = 8000
grid = np.zeros((n, n))

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		coordlist = line.split(" -> ")
		coordstart = coordlist[0]
		for coordend in coordlist[1:]:
			a_x, a_y = [int(coord) for coord in coordstart.split(",")]
			b_x, b_y = [int(coord) for coord in coordend.split(",")]
			if a_x == b_x:
				start_y = min(a_y, b_y)
				end_y = max(a_y, b_y)
				grid[a_x+offset, start_y:end_y+1] = -1
			else:
				start_x = min(a_x, b_x)
				end_x = max(a_x, b_x)
				grid[start_x+offset:end_x+1+offset, a_y] = -1
			coordstart = coordend

def add_sand():
	global result
	x, y = 500+offset, 0
	grid[x, y] = 1
	while y+1 < n:
		if grid[x, y+1] == 0:
			grid[x, y] = 0
			grid[x, y+1] = 1
			y += 1
		elif grid[x-1, y+1] == 0:
			grid[x, y] = 0
			grid[x-1, y+1] = 1
			x -= 1
			y += 1
		elif grid[x+1, y+1] == 0:
			grid[x, y] = 0
			grid[x+1, y+1] = 1
			x += 1
			y += 1
		else:
			result += 1
			return True

while add_sand():
	pass

print("result", result)
