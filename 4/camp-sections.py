elfSections = open('input.txt');

totalConcentricPairs = 0
totalOverlappingPairs = 0

def isConcentric(pairSections):
	return (
		((int(pairSections[0][0]) >= int(pairSections[1][0])) and (int(pairSections[0][1]) <= int(pairSections[1][1])))
		or
		((int(pairSections[0][0]) <= int(pairSections[1][0])) and (int(pairSections[0][1]) >= int(pairSections[1][1])))
	)

def isOverlapping(pairSections):
	return (
		(not((int(pairSections[0][0]) < int(pairSections[1][0])) and (int(pairSections[0][1]) < int(pairSections[1][0]))))
		and
		(not((int(pairSections[1][0]) < int(pairSections[0][0])) and (int(pairSections[1][1]) < int(pairSections[0][0]))))
	)


for pair in elfSections:
	pair = pair.strip()
	pairSections = []
	for elf in pair.split(','):
		pairSections.append(elf.split('-'))

	thisIsConcentric = isConcentric(pairSections)
	if thisIsConcentric:
		totalConcentricPairs += 1

	thisIsOverlapping = isOverlapping(pairSections)
	if thisIsOverlapping:
		totalOverlappingPairs += 1

	# print(str(pairSections) + ': ' + str(thisIsConcentric))
	# print(str(pairSections) + ': ' + str(thisIsConcentric))


print('concentric: ' + str(totalConcentricPairs))
print('overlapping: ' + str(totalOverlappingPairs))