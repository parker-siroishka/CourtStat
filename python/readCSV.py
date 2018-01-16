import csv
import math
def hashData(schoolCSV):
	data = []
	dictKeys = [0]
	playerDict = {}
	playerNames = [0]
	nextPlayer = 54
	index = 0
	fillerIndex = 2
	playerIndex = 1

	with open(schoolCSV) as csvfile:
		readCSV = csv.reader(csvfile, delimiter='\n')
		#append each csv row to a list
		for row in readCSV:
			if row:
				data.append(row)
		#Get number of players on each roster
		numOfPlayers = math.ceil(len(data) / 23)
		#If team csv file doesn't specify player year, fill slot so index count is 
		#not impacted
		filler = data[2][0]
		filler = filler.strip(' ')
		if filler.isdigit():
			for players in range(numOfPlayers):
				data.insert(fillerIndex, "filler")
				fillerIndex = fillerIndex +23
	
	#Add all player names to a list for use as dictionary keys
	while len(playerNames) <= numOfPlayers:
		playerNames.append(data[index])
		index = index +23
	#This line needs to be here, idk man	
	del playerNames[0]

	#dictKey is a list of lists, this puts everything in one flat list and 
	#strips excess whitespace and removes 0 at dictKey[0]
	for sublist in playerNames:
		for player in sublist:
			player = player.strip(' ')
			player = ' '.join(player.split())
			dictKeys.append(player)
	dictKeys = dictKeys[1:]


	for player in dictKeys: 	
		addToHash(playerDict, player, data, playerIndex)
		playerIndex = playerIndex +23

	for player in dictKeys:
		hashValueToInt(playerDict, player)
	return playerDict
	
def addToHash(playerDict, player, data, index):
	playerStats = []
	for k in data[index:index+22]:
		playerStats.append(k[0])
	playerDict[player] = playerStats

#All values in playerDict are strings, this
#converts all strings that can be ints and floats
#to ints and floats
def hashValueToInt(playerDict, player):
		temp = []
		for j in playerDict[player]:
			j = j.strip(' ')
			j = ' '.join(j.split())
			if j.isdigit():
				j = int(j)
			elif isFloat(j):
				j = float(j)
			temp.append(j)
		playerDict[player] = temp
				
def isFloat(value):
		try:
			float(value)
			return True
		except ValueError:
			return False