
import os
from sys import argv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from scrape import get_all_teams_data, get_team_data
from dotenv import load_dotenv
from mvb_team_urls import alberta, brandon, calgary, macewan, manitoba, mount_royal, saskatchewan, thompson_rivers, trinity_western, ubc, ubc_okanagan, ufv, winnipeg
# from server.database import retrieve_players

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')

uri = MONGODB_URL

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# will take 15-20s to complete

options = ["alberta",
           "brandon",
           "calgary",
           "macewan",
           "manitoba",
           "mru",
           "sask",
           "tru",
           "twu",
           "ubc",
           "ubco",
           "ufv",
           "winnipeg",
           "ALL"
           ]
res = []

while True:
    print("alberta")
    print("brandon")
    print("calgary")
    print("macewan")
    print("manitoba")
    print("mru")
    print("sask")
    print("tru")
    print("twu")
    print("ubc")
    print("ubco")
    print("ufv")
    print("winnipeg")
    print("ALL")
    to_update = input("Enter team to update: ")

    if to_update not in options:
        print("Enter an option in the provided list")
        continue
    else:
        if to_update == 'alberta':
            print('Updating Alberta...')
            res = [('Alberta', get_team_data(alberta))]
        elif to_update == 'brandon':
            print('Updating Brandon...')
            res = [('Brandon', get_team_data(brandon))]
        elif to_update == 'calgary':
            print('Updating Calgary...')
            res = [('Calgary', get_team_data(calgary))]
        elif to_update == 'macewan':
            print('Updating Macewan...')
            res = [('Macewan', get_team_data(macewan))]
        elif to_update == 'manitoba':
            print('Updating Manitoba...')
            res = [('Manitoba', get_team_data(manitoba))]
        elif to_update == 'mru':
            print('Updating Mount Royal...')
            res = [('Mount Royal', get_team_data(mount_royal))]
        elif to_update == 'sask':
            print('Updating Saskatchewan...')
            res = [('Saskatchewan', get_team_data(saskatchewan))]
        elif to_update == 'tru':
            print('Updating Thompson Rivers...')
            res = [('Thompson Rivers', get_team_data(thompson_rivers))]
        elif to_update == 'twu':
            print('Updating Trinity Western...')
            res = [('Trinity Western', get_team_data(trinity_western))]
        elif to_update == 'ubc':
            print('Updating UBC...')
            res = [('UBC', get_team_data(ubc))]
        elif to_update == 'ubco':
            print('Updating UBCO...')
            res = [('UBCO', get_team_data(ubc_okanagan))]
        elif to_update == 'ufv':
            print('Updating UFV...')
            res = [('UFV', get_team_data(ufv))]
        elif to_update == 'winnipeg':
            print('Updating Winnipeg...')
            res = [('Winnipeg', get_team_data(winnipeg))]
        elif to_update == 'ALL':
            print('Updating all teams...')
            res = get_all_teams_data()
        break


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
            current_player_document = player_stats_collection.find_one(
                {'Team': team_name, 'Name': player_data[1]})
            # if so, make changes to current player
            if current_player_document:
                player_document = current_player_document
            else:
                player_document = {'Team': team_name}
                # Initialize the statistics sub-document
                player_document['Statistics'] = {}
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
                        # Calculate the currentTotal
                        current_total = sum(historical_values)
                    else:
                        # Initialize historical values list
                        historical_values = [float(current_statistic)]
                        # Initialize currentTotal with the current value
                        current_total = float(current_statistic)

                    # Update the fields in the document
                    player_document['Statistics'][historical_key] = historical_values
                    player_document['Statistics'][current_total_key] = current_total
                else:
                    player_document[header] = player_data[index]
            # Label Name field to 'Totals' in totals document for each team (Totals document has no personal data)
                if player_document['#'] == 'N/A' and player_document['Name'] == 'N/A' and player_document['Yr'] == 'N/A' and player_document['Pos'] == 'N/A':
                    player_document['Team'] = 'Totals'
            query = {
                "Team": player_document["Team"], "#": player_document["#"], "Name": player_document["Name"]}
            update = player_document
            print(update)
            player_stats_collection.update_one(
                query, {"$set": update}, upsert=True)
            # player_stats_collection.insert_one(player_document)

except Exception as e:
    print(e)
