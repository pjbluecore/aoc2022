import sys

rpsGuide = open('input.txt');

antagonistMoves = ['A','B','C']
protagonistMoves = ['X','Y','Z']


def getMoveScore(moveCode):
	return protagonistMoves.index(moveCode) + 1

def getResultScore(proMoveCode, anMoveCode):
	anMoveValue = antagonistMoves.index(anMoveCode) - 1
	proMoveValue = protagonistMoves.index(proMoveCode)
	# index 1 beats 0, index 2 beats 1, index 0 beats 2
	matchupValue = (proMoveValue - anMoveValue) % 3

	# ties will look like 0s now, and wins like 1s, losses like -1s
	# we need losses to be 0, ties 1, and wins 2
	offsetMatchupValue = matchupValue - 1
	weightedMatchupValue = matchupValue * 3

	return weightedMatchupValue

totalScore = 0

for row in rpsGuide:
	moves = row.strip().split(' ')
	anMove = moves[0]
	proMove = moves[1]

	thisMoveScore = getMoveScore(proMove)
	thisResultScore = getResultScore(proMove, anMove)

	print('row: ' + str(row.strip()))
	print('  move score: ' + str(thisMoveScore))
	print('  result score: ' + str(thisResultScore) + '\n')

	totalScore += (thisMoveScore + thisResultScore)

print(totalScore)