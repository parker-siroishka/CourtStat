from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
from mvbTeamURLS import team_urls


def get_team_data(team_url: str):
	result = []
	quote_page = team_url
 	# might need this in an .env variable in the future
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.62'
	request = Request(quote_page, headers={'User-Agent': user_agent})
	page = urlopen(request)
	soup = BeautifulSoup(page, 'html.parser')
	# roster data is 4th table on team page
	roster_table = soup.findAll('table')[3]
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

	return roster_data

def get_all_teams_data():
    res = []
    for team_url in team_urls:
        team_data = get_all_teams_data(team_url)
        res.append(team_data)

