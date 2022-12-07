rucksackIndex = open('input.txt');


def splitRucksackToPockets(rucksack):
	pockets = []
	#have to cast as int because divide returns float
	pocketSize = int(len(rucksack)/2)

	pockets.append(rucksack[:pocketSize])
	pockets.append(rucksack[pocketSize:])
	return pockets


def getCommonValues(list1, list2):
	commonValues = []
	for item in list1:
		if item in list2:
			commonValues.append(item)

	return commonValues


def getCommonPocketValue(rucksack):
	pockets = splitRucksackToPockets(rucksack)
	pocket0 = [*pockets[0]]
	pocket1 = [*pockets[1]]

	# print(rucksack)
	# print(' - ' + pockets[0])
	# for item in pocket0:
	# 		print('   - ' + item)
	# print(' - ' + pockets[1])
	# for item in pocket1:
	# 		print('   - ' + item)

	commonItem = getCommonValues(pocket0, pocket1)[0]

	return commonItem


def splitElvesIntoGroups(elfList, groupSize):
	elfGroups = []
	for i, elf in enumerate(elfList):
		elf = elf.strip()
		if i % 3 == 0:
			elfGroups.append([elf])
		else:
			elfGroups[len(elfGroups)-1].append(elf)
	return elfGroups

def getItemPriority(item):
	priorities = []

	# lowercases
	for i in range(26):
		priorities.append(chr(i+97))
	for i in range(26):
		priorities.append(chr(i+65))
	# print(priorities)

	return priorities.index(item)


def calculateTotalCharacterValues(charList):
	totalPrioritiesValue = 0
	for char in charList:
		thisPriority = getItemPriority(char) + 1
		totalPrioritiesValue += thisPriority

	return totalPrioritiesValue


def calculateTotalCommonPrioritiesValues():
	prioritiesList = []
	for row in rucksackIndex:
		thisRucksack = row.strip()
		thisCommonItem = getCommonPocketValue(thisRucksack)

		print(thisRucksack)
		print(thisCommonItem + ': ' + str(thisPriority))

	return calculateTotalCharacterValues(prioritiesList)


elfGroups = splitElvesIntoGroups(rucksackIndex,3)
# print(elfGroelfListups)
badges = []

for elfGroup in elfGroups:
	commonValues = getCommonValues(elfGroup[0], elfGroup[1]);
	badge = getCommonValues(commonValues, elfGroup[2])[0]
	# print(elfGroup)
	# print(' - ' + badge)
	badges.append(badge)
totalBadgesValue = calculateTotalCharacterValues(badges)
print(totalBadgesValue)
