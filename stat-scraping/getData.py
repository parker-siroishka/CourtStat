from urllib.request import Request, urlopen
import csv
import re
from bs4 import BeautifulSoup
# from teamURLs import teamurls, teamNames


def writeStats():
	
	quote_page ='https://canadawest2023.prestosports.com/sports/mvball/2021-22/teams/calgary'
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.62'
	# scrape the HTML page from the passed url
	request = Request(quote_page, headers={'User-Agent': user_agent})
	page = urlopen(request)
	soup = BeautifulSoup(page, 'html.parser')
	# roster data is 4th table on team page
	roster_table = soup.findAll('table')[3]
	print(roster_table)
	roster_data = []

	for row in roster_table.findAll('tr'):
		cols = row.findAll('td')

		if len(cols) == 0:
			cols = row.findAll('th')
		
		cols = [ele.text.strip() for ele in cols]
		

		roster_data.append([
			re.sub(' +', ' ', 
	  			ele.replace('\n', '').replace('\r', '')) 
			for ele in cols if ele
		])

	print(roster_data)
	

	# with open((name + 'Data.csv'), 'w') as csv_file:
	# 	csv_writer = csv.writer(csv_file)
	# 	for j in rosterStatsList:
	# 		csv_writer.writerow([j])

writeStats()
# for i in range(0,12):
# 	writeStats(teamurls[i], teamNames[i])	
# 	print("writing "+teamNames[i]+"...("+str(12-i)+")")		
