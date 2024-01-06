import numpy as np

monkeys = []

def operator_casting(operator):
	if operator == "+":
		return lambda a, b : a + b
	elif operator == "*":
		return lambda a, b : a * b
	else:
		ValueError()

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		s = line.split()
		if line == "":
			continue
		elif s[0] == "Monkey":
			monkeys.append({"id" : int(s[1].replace(":", ""))})
			monkeys[-1]["inspects"] = 0
		elif s[0] == "Starting" and s[1] == "items:":
			monkeys[-1]["items"] = [int(string.replace(",", "")) for string in s[2:]]
		elif s[0] == "Operation:":
			monkeys[-1]["operator"] = s[4]
			monkeys[-1]["op_par"] = s[5]
		elif s[0] == "Test:":
			monkeys[-1]["divisible"] = int(s[-1])
		elif s[1] == "true:":
			monkeys[-1]["target1"] = int(s[-1])
		elif s[1] == "false:":
			monkeys[-1]["target2"] = int(s[-1])
		else:
			print(i, s)

for round in range(1, 21):
	for monkey in monkeys:
		opfunc = operator_casting(monkey["operator"])
		divisor = monkey["divisible"]
		numpopped = 0
		for i_item, item in enumerate(list(monkey["items"])):
			parameter = item if monkey["op_par"] == "old" else int(monkey["op_par"])
			newlevel = opfunc(item, parameter) // 3
			thetest = (newlevel % divisor) == 0
			tar = monkey["target1"] if thetest else monkey["target2"]
			monkey["items"].pop(i_item - numpopped)
			monkeys[tar]["items"].append(newlevel)
			numpopped += 1
			monkey["inspects"] += 1

inspects = [m["inspects"] for m in monkeys]
print(np.product(np.sort(inspects)[-2:]))
