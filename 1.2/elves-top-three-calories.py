import sys
import copy

elfIndex = open('input.txt');
# elfIndex = open('test-1.txt');

elfList = []
currentElfCalories = 0
currentElfIndex = 1

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

def makeElf():
	newElf = {
		"index": currentElfIndex,
		"calories": currentElfCalories
	}
	return newElf

def insertElfCaloriesInOrder(newElf):
	if len(elfList) == 0:
		elfList.append(newElf)
	else:
		for i, elf in enumerate(elfList):
			if elf["calories"] > newElf["calories"]:
				elfList.insert(i, newElf)
				return
		elfList.append(newElf)

def addToElf(val):
	global currentElfCalories

	currentElfCalories += int(val)
	# print('adding to current elf: ' + str(val))

def finishElf():
	global currentElfCalories
	global currentElfIndex

	newElf = makeElf()
	# print("finishing elf: " + str(newElf))
	insertElfCaloriesInOrder(newElf)
	currentElfCalories = 0
	currentElfIndex += 1

for row in elfIndex:
	row = row.strip()
	if row:
		addToElf(row)
	else:
		finishElf()
		# print(elfList)
finishElf()
# print(elfList)

# print(len(elfList))
# print(elfList)

def sumTopNElvesCalories(n):
	nSum = 0
	elfListHolder = copy.copy(elfList)

	for i in range(n):
		nSum += elfListHolder.pop()["calories"]

	return nSum

print(sumTopNElvesCalories(3))