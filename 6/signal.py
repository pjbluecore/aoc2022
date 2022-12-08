stream = open('input.txt');

packetMaybe = []
packetLength = 14

def packetIsFull(packet):
	return len(packet) == packetLength

def isSet(setMaybe):
	return len(setMaybe) == len(set(setMaybe))

def convertStringToList(string):
	newList = []
	newList[:0] = string
	return newList

def getPacketIndex(stream):
	global packetMaybe
	# print(stream)
	# print([stream[0:]])

	stream = convertStringToList(stream)
	for i, char in enumerate(stream):
		if packetIsFull(packetMaybe):
			packetMaybe = packetMaybe[1:]
		packetMaybe.append(char)
		print(char)
		print(packetMaybe)

		if isSet(packetMaybe) and len(packetMaybe) == packetLength:
			return i+1

# getPacketIndex()
for row in stream:
	row = row.strip()
	print(getPacketIndex(row))

# testY = [1,2,3]
# testN = [1,1,2]
# print(str(isSet(testN)))