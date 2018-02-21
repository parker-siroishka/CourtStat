from readCSV import hashData
from hashedData import teams,kills,errors,assists,aces,digs,blocksSolo,blocksAss, calcPoints
import string

possibleStats = [kills,errors,assists,aces,digs,blocksSolo,blocksAss]
possibleStatsStrings = ["kills","errors","assists","aces","digs","blocksSolo","blocksAss"]
roster = []
rosterTotalPoints = 0

#Sifts through all hashtables and keys (which are players names). If a key == player name you are wanting, 
#all needed (possibleStatsStrings) stats are put into a list
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


roster = []
#for team in teams:
	#for player in team:
	
#print(temp)
#Loop through and pick team until 8 player roster is made	
while len(roster) < 8:
	fantasyPlayer = input("Pick your 8 player roster: ")
	fantasyPlayer = string.capwords(fantasyPlayer)
	#print(fantasyPlayer)
	roster.append(player(fantasyPlayer))
	#else:
	#	print("That player does not exist")

print(roster)


#Display each player in roster and their points and teams total points in an easy and digestible way
try:
	for i in range(8):
		for team in teams:
			for player in team:
				if roster[i][0] == player:
					print(player + " " + str(calcPoints(team,roster[i][0])))
					rosterTotalPoints += calcPoints(team,roster[i][0])
				
	print("Total Team Points: " + str(rosterTotalPoints))
except IndexError as e:
	print("You somehow still got an error")

