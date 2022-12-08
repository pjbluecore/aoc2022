import textwrap

crateInput = open('input.txt');
crateStacks = []

def isStacks(row):
	return '[' in row

def doStacks(row):
	global crateStacks

	crateArray = [row[i:i+3] for i in range(0, len(row), 4)]
	# print('crateArray: ' + str(crateArray))
	# print('len(crateArray): ' + str(len(crateArray)))

	# print('len(crateStacks): ' + str(len(crateStacks)))
	if len(crateStacks) == 0:
		for i in range(0, len(crateArray)):
			crateStacks.append([])

	# print('time to start stacking!')
	for i, crate in enumerate(crateArray):
		# print(crate)
		if crate.strip() != '':
			crate = [crate[1:2]][0]
			# print(crate)
			crateStacks[i].insert(0,crate)

def isInstructions(row):
	return 'move' in row

def moveCrate(whence, whither):
	global crateStacks

	crateStacks[whither].append(crateStacks[whence].pop())

def doInstructions9000(row):
	thisInstructions = row.split(' ')
	howMany = int(thisInstructions[1])
	whence = int(thisInstructions[3]) - 1
	whither = int(thisInstructions[5]) - 1

	for i in range(0, howMany):
		moveCrate(whence, whither)

def doInstructions9001(row):
	global crateStacks
	thisInstructions = row.split(' ')
	howMany = int(thisInstructions[1])
	whence = int(thisInstructions[3]) - 1
	whither = int(thisInstructions[5]) - 1

	stackHolder = []
	for i in range(0, howMany):
		stackHolder.insert(0, crateStacks[whence].pop())

	crateStacks[whither] += stackHolder

def getTopCrates():
	topCrates = ''
	for stack in crateStacks:
		thisTopCrate = stack[len(stack)-1]
		print(thisTopCrate)
		topCrates = topCrates + thisTopCrate
	return topCrates

def crateMover9000():
	for row in crateInput:
		row = row.replace('\n', '')
		# print('row: ' + str(row))
		if isStacks(row):
			doStacks(row)
		elif isInstructions(row):
			doInstructions9000(row)

	print('crateStacks: ' + str(crateStacks))
	print(getTopCrates())

def crateMover9001():
	for row in crateInput:
		row = row.replace('\n', '')
		# print('row: ' + str(row))
		if isStacks(row):
			doStacks(row)
		elif isInstructions(row):
			doInstructions9001(row)

	print('crateStacks: ' + str(crateStacks))
	print(getTopCrates())

crateMover9001()