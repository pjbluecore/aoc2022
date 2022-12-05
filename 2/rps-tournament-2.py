import sys

rpsGuide = open('input.txt');

antagonistMoves = ['A','B','C']
results = ['X','Y','Z']

def getResultScore(resultCode):
	return results.index(resultCode) * 3

def getMoveScore(anMoveCode, resultCode):
	anMoveIndex = antagonistMoves.index(anMoveCode)
	proMoveShift = results.index(resultCode) - 1
	proMoveIndex = (anMoveIndex + proMoveShift) % 3
	proMoveScore = proMoveIndex + 1

	return proMoveScore



totalScore = 0

for row in rpsGuide:
	moves = row.strip().split(' ')
	anMove = moves[0]
	result = moves[1]

	thisMoveScore = getMoveScore(anMove, result)
	thisResultScore = getResultScore(result)

	print('row: ' + str(row.strip()))
	print('  move score: ' + str(thisMoveScore))
	print('  result score: ' + str(thisResultScore) + '\n')

	totalScore += (thisMoveScore + thisResultScore)

print(totalScore)