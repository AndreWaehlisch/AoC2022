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
			monkeys[-1]["operation"] = operator_casting(s[4])
			monkeys[-1]["op_par"] = s[5]
		elif s[0] == "Test:":
			monkeys[-1]["divisible"] = int(s[-1])
		elif s[1] == "true:":
			monkeys[-1]["target1"] = int(s[-1])
		elif s[1] == "false:":
			monkeys[-1]["target2"] = int(s[-1])
		else:
			print(i, s)

# modulus trick from https://youtu.be/W9vVJ8gDxj4
# this only works because divisors are prime, right?
lcm = np.product([m["divisible"] for m in monkeys])

for round in tqdm(range(1, 10001)):
	for monkey in monkeys:
		opfunc = monkey["operation"]
		divisor = monkey["divisible"]
		numpopped = 0
		for i_item, item in enumerate(list(monkey["items"])):
			parameter = item if monkey["op_par"] == "old" else int(monkey["op_par"])
			newlevel = opfunc(item, parameter) % lcm
			thetest = (newlevel % divisor) == 0
			tar = monkey["target1"] if thetest else monkey["target2"]
			monkey["items"].pop(i_item - numpopped)
			monkeys[tar]["items"].append(newlevel)
			numpopped += 1
			monkey["inspects"] += 1

inspects = [m["inspects"] for m in monkeys]
print(np.product(np.sort(inspects)[-2:]))
