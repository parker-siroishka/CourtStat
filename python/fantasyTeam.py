from readCSV import hashData
from hashedData import teams,kills,errors,assists,aces,digs,blocksSolo,blocksAss, calcPoints

possibleStats = [kills,errors,assists,aces,digs,blocksSolo,blocksAss]
possibleStatsStrings = ["kills","errors","assists","aces","digs","blocksSolo","blocksAss"]
roster = []
rosterTotalPoints = 0


def player(fantasyPlayer):
	stats = []
	for team in teams:
		for player in team:
			if fantasyPlayer == player:
				stats.append(fantasyPlayer)
				for i in range(7):
					string = (possibleStatsStrings[i]+" "+str(team[fantasyPlayer][possibleStats[i]]))
					stats.append(string)	
	return stats		


temp = []
while len(temp) < 8:
	fantasyPlayer = input("Pick your 8 player roster: ")
	temp.append(player(fantasyPlayer))

#for i in range(8):
#	for team in teams:
#		for player in teams:
#			if temp[i][0] == player:
#				print(temp[i][0] + " " + str(calcPoints(team,temp[i][0])))
#				rosterTotalPoints += calcPoints(albertaRoster,temp[i][0])
#print("Total Team Points: " + rosterTotalPoints)
print(temp)