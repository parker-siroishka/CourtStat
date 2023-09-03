
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')

uri = MONGODB_URL

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.CourtStat

player_collection = db.get_collection('PlayerStats')

# helpers

def player_helper(player) -> dict:
    return {
        "Team": player["Team"],
        "Number": player["#"],
        "Name": player["Name"],
        "Yr": player["Yr"],
        "Pos": player["Pos"],
        "Matches": player["m"],
        "Sets": player["s"],
        "Kills": player["k"],
        "KillsPerSet": player["k/s"],
        "Errors": player["e"],
        "Attempts": player["ta"],
        "Percentage": player["pct"],
        "Assists": player["a"],
        "AssistsPerSet": player["a/s"],
        "ServiceAces": player["sa"],
        "ServiceAcesPerSet": player["sa/s"],
        "Receptions": player["r"],
        "Digs": player["digs"],
        "DigsPerSet": player["d/s"],
        "BlockSolo": player["bs"],
        "BlockAssists": player["ba"],
        "BlockTotal": player["tot"],
        "BlocksPerSet": player["b/s"],
        "Points": player["pts"],
        "PointsPerSet": player["pts/s"]
    }

# Retrieve all players present in the database
async def retrieve_players():
    players = []
    async for player in player_collection.find():
        players.append(player_helper(player))
    return players


# Add a new player into to the database
def add_player(player_data: dict) -> dict:
    player = player_collection.insert_one(player_data)
    new_player = player_collection.find_one({"_id": player.inserted_id})
    return player_helper(new_player)


# Retrieve a player with a matching ID
def retrieve_player(id: str) -> dict:
    player = player_collection.find_one({"_id": ObjectId(id)})
    if player:
        return player_helper(player)


# Update a player with a matching ID
def update_player(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    player = player_collection.find_one({"_id": ObjectId(id)})
    if player:
        updated_player = player_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_player:
            return True
        return False


# Delete a player from the database
def delete_player(id: str):
    player =  player_collection.find_one({"_id": ObjectId(id)})
    if player:
        player_collection.delete_one({"_id": ObjectId(id)})
        return True
