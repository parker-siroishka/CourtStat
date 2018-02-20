from readCSV import hashData, addToHash
import operator

position = 1
kills = 4
killsMult = 1
errors = 6
errorsMult = -1
assists = 9
assistsMult = 0.25
aces = 11
acesMult = 2
digs = 13
digsMult = 1
blocksSolo = 15
blocksSoloMult = 2
blocksAss = 16
blocksAssMult = 1

#Each teams hashtable
calgaryRoster = hashData("calgaryData.csv")
trinityWesternRoster = hashData("trinityWesternData.csv")
reginaRoster = hashData("reginaData.csv")
albertaRoster = hashData("albertaData.csv")
brandonRoster = hashData("brandonData.csv")
grantMacewanRoster = hashData("macewanData.csv")
manitobaRoster = hashData("manitobaData.csv")
mountRoyalRoster = hashData("mountRoyalData.csv")
saskatchewanRoster = hashData("saskatchewanData.csv")
thompsonRiversRoster = hashData("thompsonRiversData.csv")
ubcRoster = hashData("ubcData.csv")
ubcOkanaganRoster = hashData("ubcOkanaganData.csv")
winnipegRoster = hashData("winnipegData.csv")

teams = [calgaryRoster,trinityWesternRoster,reginaRoster,albertaRoster,brandonRoster,grantMacewanRoster,manitobaRoster\
			,mountRoyalRoster,saskatchewanRoster,thompsonRiversRoster,ubcRoster,ubcOkanaganRoster,winnipegRoster]
leaderboards = []


#Calculates players fantasy points based off of predefined multipliers
def calcPoints(schoolRoster, playerName):
	killPoints = (schoolRoster[playerName][kills]) * killsMult 
	assistPoints = (schoolRoster[playerName][assists]) * assistsMult 
	acesPoints = (schoolRoster[playerName][aces]) * acesMult 
	digPoints = (schoolRoster[playerName][digs]) * digsMult
	blocksSoloPoints = (schoolRoster[playerName][blocksSolo]) * blocksSoloMult
	blocksAssPoints = (schoolRoster[playerName][blocksAss]) * blocksAssMult
	errorPoints = (schoolRoster[playerName][errors]) * errorsMult 

	totalPoints = killPoints+assistPoints+acesPoints+digPoints+blocksSoloPoints+blocksAssPoints+errorPoints

	return totalPoints 

#prints all keys (player names) in school roster specified
def displayNames(schoolRoster):
	for keys in schoolRoster.keys():
		print(keys)

#Prints all player names and calculated stats beside them
def displayStats(roster):
	for player in roster:
		try:
			print(player,": ",calcPoints(roster, player))
		except TypeError:
			print(player,": Not enough data")

#Creates a league-wide leaderboard for points
def createLeaderboards(teams):
	for team in teams:
		for player in team:
			#Doesnt add players with insufficient data
			try:
				leaderboards.append((player,calcPoints(team,player)))
			except TypeError:
				pass
	return leaderboards

#sorts leaderboards from most points to least points
def sortLeaderboards(leaderboards):
	leaderboards.sort(key=operator.itemgetter(1))
	for i in reversed(leaderboards):
		print(i[1],": ",i[0])
#barebones program testing implementation of methods and making an easy way to view all league-wide stats
def run():
	player = None
	roster = None
	schools = ["UC","TWU","REG","UAB","BU","GMU","MAN","MRU","SASK","TRU","UBC","UBCO","WPG","L"]
	while True:
		print(" -UC-", "\n","-TWU-", "\n","-REG-","\n","-UAB-", "\n","-BU-","\n","-GMU-","\n","-MAN-","\n",\
				"-MRU-","\n","-SASK-","\n","-TRU-","\n","-UBC-","\n","-UBCO-","\n","-WPG-","\n","-(L)EADERBOARDS-")
		temp = input("Pick a Team: ")
		if temp in schools:
			if temp == "UC":
				displayStats(calgaryRoster)
			elif temp == "TWU":
				displayStats(trinityWesternRoster)
			elif temp == "REG":
				displayStats(reginaRoster)
			elif temp == "UAB":
				displayStats(albertaRoster)
			elif temp == "BU":
				displayStats(brandonRoster)
			elif temp == "GMU":
				displayStats(grantMacewanRoster)
			elif temp == "MAN":
				displayStats(manitobaRoster)
			elif temp == "MRU":
				displayStats(mountRoyalRoster)
			elif temp == "SASK":
				displayStats(saskatchewanRoster)
			elif temp == "TRU":
				displayStats(thompsonRiversRoster)
			elif temp == "UBC":
				displayStats(ubcRoster)
			elif temp == "UBCO":
				displayStats(ubcOkanaganRoster)
			elif temp == "WPG":
				displayStats(winnipegRoster)
			elif temp == "L":
					sortLeaderboards(createLeaderboards(teams))
		else:
			print("Invalid Input")

#run()
	

