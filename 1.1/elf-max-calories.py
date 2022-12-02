import sys

elfIndex = open('input.txt');

maxElfCalories = 0
currentElfCalories = 0

for row in elfIndex:
	if row == '\n':
		currentElfCalories = 0
	else:
		currentElfCalories += int(row)
		if currentElfCalories > maxElfCalories:
			maxElfCalories = currentElfCalories

print(maxElfCalories)