
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from scrapeSite import get_all_teams_data

uri = ""

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# will take 15-20s to complete
res = get_all_teams_data()

HEADERS = 0
STAT_TOTALS = -1


        

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to CourtStat MongoDB!")
    db = client.CourtStat
    player_stats_collection = db["PlayerStats"]
    for team_data in res:
        team_name = team_data[0]
        team = team_data[1]
        # delete opponent totals row (last row)
        del team[STAT_TOTALS]
         # stat cagtegories are first row, stat totals is new last row
        headers = team[HEADERS]
        # delete header row from team data after collecting header values
        del team[HEADERS]
        # pad stat totals to align correctly (no values for #, Name, Yr, Pos)
        team[STAT_TOTALS] = ['N/A'] + team[STAT_TOTALS]
        for player_data in team:
            player_document = {'Team': team_name}
            for index, header in enumerate(headers):
                player_document[header] = player_data[index]
            # Label Name field to 'Totals' in totals document for each team (Totals document has no personal data)
            if player_document['#'] == 'N/A' and player_document['Name'] == 'N/A' and player_document['Yr']  == 'N/A' and player_document['Pos'] == 'N/A':
                player_document['Name'] = 'Totals'
                
            player_stats_collection.insert_one(player_document)
    
    
except Exception as e:
    print(e)
    