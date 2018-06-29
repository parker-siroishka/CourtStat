from readCSV import hashData, addToHash
from firebase import firebase
import operator
import itertools 

firebase = firebase.FirebaseApplication('https://statgen-993f4.firebaseio.com/')


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
	killPoints = (schoolRoster[playerName][kills]) * killsMult 
	assistPoints = (schoolRoster[playerName][assists]) * assistsMult 
	acesPoints = (schoolRoster[playerName][aces]) * acesMult 
	digPoints = (schoolRoster[playerName][digs]) * digsMult
	blocksSoloPoints = (schoolRoster[playerName][blocksSolo]) * blocksSoloMult
	blocksAssPoints = (schoolRoster[playerName][blocksAss]) * blocksAssMult
	errorPoints = (schoolRoster[playerName][errors]) * errorsMult 

	totalPoints = killPoints+assistPoints+acesPoints+digPoints+blocksSoloPoints+blocksAssPoints+errorPoints

	allStats = [totalPoints, killPoints, assistPoints, acesPoints, digPoints, blocksSoloPoints, blocksAssPoints, errorPoints]

	return  allStats


def putData():
	schools = ['UC','TWU','UAB','BU','GMU','MAN','MRU','SASK','TRU','UBC','UBCO','WPG']
	for school, roster in itertools.izip(schools, teams):
		for player in roster:

			try:
				result =firebase.put(('/league/volleyball/'+school), player, {'total points':str(calcStatsList(roster, player)[0]),'kill points':str(calcStatsList(roster, player)[1]),'assist points':str(calcStatsList(roster, player)[2]),'ace points':str(calcStatsList(roster, player)[3]), 'dig points': str(calcStatsList(roster, player)[4]), 'blocks solo points': str(calcStatsList(roster, player)[5]), 'blocks assists points': str(calcStatsList(roster, player)[6]), 'error points': str(calcStatsList(roster, player)[7])})
			except TypeError:
				pass

putData()

	

