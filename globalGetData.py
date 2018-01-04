import urllib.request
import csv
from bs4 import BeautifulSoup
from datetime import datetime
from teamURLs import teamurls, teamNames


def writeStats(url, name):
	quote_page = url
	# get the HTML page of the url declared
	page = urllib.request.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	# Find all <div> tags that are labeled class 'scrollable'. There are
	# multiple miscellaneous <div> classes butwe only want the 0th because
	# that is all players stats
	listOfScrollableDivs = soup.findAll('div', {'class': 'scrollable'})
	rosterStats = listOfScrollableDivs[0]
	# Strip and format the huge ass string we scraped from the <div> and
	# split it into a list seperated by '\n'
	rosterStats = rosterStats.text.strip()
	rosterStatsList = rosterStats.split('\n')
	# Chop everything before the first players number, which is index[29] in all cases
	# Chop everything after the last players last stat and remake list
	end = rosterStatsList.index("Totals")
	rosterStatsList = rosterStatsList[29:end-1]
		

	with open((name + 'Data.csv'), 'w') as csv_file:
		csv_writer = csv.writer(csv_file)
		for j in rosterStatsList:
			csv_writer.writerow([j])


for i in range(0,13):
	writeStats(teamurls[i], teamNames[i])	
	print("writing "+teamNames[i]+"...("+str(12-i)+")")		
