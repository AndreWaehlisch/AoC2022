import numpy as np
import re
from collections import defaultdict, deque

class dir:
	def __init__(self, name, parent=None):
		self.size = 0
		self.name = name
		self.parent = parent
		self.children = deque()

root = dir("/")
cwd = root

expecting_ls = False
ls_list = []
totalsize = 0

def collect_ls():
	global ls_list, cwd, totalsize, expecting_ls
	expecting_ls = False
	for i_ls in ls_list:
		ls_A, ls_B = i_ls.split()
		if ls_A != "dir":
			incsize = int(ls_A)
			cwd.size += incsize
			totalsize += incsize

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		if line[:4] == "$ cd":
			if expecting_ls:
				collect_ls()
			target = line.split()[-1]
			if target == "/":
				cwd = root
			elif target == "..":
				cwd = cwd.parent
			else:
				cwd = dir(target, parent=cwd)
				cwd.parent.children.append(cwd)
		elif line[:4] == "$ ls":
			expecting_ls = True
			ls_list = []
		elif expecting_ls:
			ls_list.append(line)

collect_ls()
result = totalsize
targetsize = 30000000 - (70000000 - totalsize)

def findcandidate(dir):
	global result
	mysize = dir.size
	for i in dir.children:
		mysize += findcandidate(i)
	if (mysize < result) and (mysize >= targetsize):
		result = mysize
	return mysize

__ = findcandidate(root)
print("result:", result)
