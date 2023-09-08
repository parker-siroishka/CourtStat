
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from scrape import get_all_teams_data
from dotenv import load_dotenv
# from server.database import retrieve_players

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')

uri = MONGODB_URL

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# will take 15-20s to complete
res = get_all_teams_data()

HEADERS = 0
STAT_TOTALS = -1

NUMERIC_STATS = ['m', 's', 'k', 'k/s', 
                 'e', 'ta', 'pct', 'a', 
                 'a/s', 'sa', 'sa/s', 'r', 
                 're', 'digs', 'd/s', 'bs', 
                 'ba', 'tot', 'b/s', 'pts', 
                 'pts/s']

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
            # check to see if current player already exists in collection
            current_player_document = player_stats_collection.find_one({'Team': team_name, 'Name': player_data[1]})
            # if so, make changes to current player
            if current_player_document:
                player_document = current_player_document
            else:
                player_document = {'Team': team_name}
                player_document['Statistics'] = {}  # Initialize the statistics sub-document
            for index, header in enumerate(headers):
                # Check if the header is a numeric statistic (m, s, k, etc.)
                if header in NUMERIC_STATS:
                    current_statistic = player_data[index]
                    # replace non-existent values with 0.00
                    if current_statistic == '-':
                        current_statistic = 0.00
                    historical_key = f"{header}_historical"
                    current_total_key = f"{header}_currentTotal"
                    # Check if there are existing historical values in the document
                    if historical_key in player_document['Statistics']:
                        historical_values = player_document['Statistics'][historical_key]
                        historical_values.append(float(current_statistic))
                        current_total = sum(historical_values)  # Calculate the currentTotal
                    else:
                        historical_values = [float(current_statistic)]  # Initialize historical values list
                        current_total = float(current_statistic)  # Initialize currentTotal with the current value

                    # Update the fields in the document
                    player_document['Statistics'][historical_key] = historical_values
                    player_document['Statistics'][current_total_key] = current_total
                else:
                    player_document[header] = player_data[index]
            # Label Name field to 'Totals' in totals document for each team (Totals document has no personal data)
                if player_document['#'] == 'N/A' and player_document['Name'] == 'N/A' and player_document['Yr']  == 'N/A' and player_document['Pos'] == 'N/A':
                    player_document['Name'] = 'Totals'
            query = { "Team": player_document["Team"], "#": player_document["#"], "Name": player_document["Name"]}
            update = player_document
            player_stats_collection.update_one(query, {"$set": update}, upsert=True)
            # player_stats_collection.insert_one(player_document)
                
except Exception as e:
    print(e)
