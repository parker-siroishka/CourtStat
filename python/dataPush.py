from readCSV import hashData, addToHash
from firebase import firebase
import operator
import itertools

firebase = firebase.FirebaseApplication('https://statgen-993f4.firebaseio.com/')

kills = 4
errors = 6
assists = 9
aces = 11
digs = 13
blocksSolo = 15
blocksAss = 16

#Each teams hashtable
calgaryRoster = hashData("calgaryData.csv")
trinityWesternRoster = hashData("trinityWesternData.csv")
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

teams = [calgaryRoster,trinityWesternRoster,albertaRoster,brandonRoster,grantMacewanRoster,manitobaRoster\
			,mountRoyalRoster,saskatchewanRoster,thompsonRiversRoster,ubcRoster,ubcOkanaganRoster,winnipegRoster]

def calcStatsList(schoolRoster, playerName):
	# Checks if the team roster has the players year listed or not. 
	# If the year is listed, the position will be index [1]. If the
	# name is not listed, the position will be index[0].
	if(schoolRoster[playerName][1] == 'f'):
		
		playerPosition = (schoolRoster[playerName][0])
	else:
		playerPosition = (schoolRoster[playerName][1])

	killsTOT = (schoolRoster[playerName][kills])
	assistsTOT = (schoolRoster[playerName][assists])
	acesTOT = (schoolRoster[playerName][aces])
	digsTOT = (schoolRoster[playerName][digs])
	blocksSoloTOT = (schoolRoster[playerName][blocksSolo])
	blocksAssistsTOT = (schoolRoster[playerName][blocksAss])
	errorsTOT = (schoolRoster[playerName][errors])

	allStats = [killsTOT, assistsTOT, acesTOT, digsTOT, blocksSoloTOT, blocksAssistsTOT, errorsTOT, playerPosition]

	return  allStats


def putData():
	schools = ['UC','TWU','UAB','BU','GMU','MAN','MRU','SASK','TRU','UBC','UBCO','WPG']
	for school, roster in zip(schools, teams):
		for player in roster:

			try:
				playerStats = calcStatsList(roster, player)
				print(playerStats)
				result =firebase.put(('/playerData/'+school), player, {'position':str(playerStats[7]),'killsTOT':str(playerStats[0]),'assistsTOT':str(playerStats[1]),'acesTOT':str(playerStats[2]),\
																	   'digsTOT': str(playerStats[3]), 'blocks soloTOT': str(playerStats[4]), 'blocks assistsTOT': str(playerStats[5]), 'errorsTOT': str(playerStats[6])})
			except TypeError:
				pass

putData()

	

