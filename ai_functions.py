import os
import json
import re
import responses as resp

#load data from the json file
def load_data_stats(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

#save data from the json file when the machine don't know the player name
def save_data_stats(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)

#helper function for comparing players
def calculate_stats(num1: int ,num2: int) -> int :
    result = num1 / num2 
    return result

#find players in the database
def find_player(name: str) -> dict | None:
    player_info: dict = load_data_stats('player_stats.json')

    for record in player_info["player_stats"]:
        player_name = record["player_name"].lower()

        if name.lower() in player_name:
            return record

    return None

#function that will compare who's better among the two
def compare_players(playerOne: dict, playerTwo: dict):
    playerOne_advantage = 0
    playerTwo_advantage = 0

    #comparing total points
    if calculate_stats(playerOne["total_point"], playerOne["num_games_played"]) > calculate_stats(playerTwo["total_point"], playerTwo["num_games_played"]):
        playerOne_advantage += 1
    else:
        playerTwo_advantage += 1

    #comparing three point field goal   
    if calculate_stats(playerOne["total_three_point"], playerOne["three_points_attempt"]) > calculate_stats(playerTwo["total_three_point"], playerTwo["three_points_attempt"]):
        playerOne_advantage += 1
    else: 
        playerTwo_advantage += 1
    
    #comparing assist   
    if calculate_stats(playerOne["total_assist"], playerOne["num_games_played"]) > calculate_stats(playerTwo["total_assist"], playerTwo["num_games_played"]):
        playerOne_advantage += 1
    else: 
        playerTwo_advantage += 1
    
    #comparing rebound   
    if calculate_stats(playerOne["total_rebound"], playerOne["num_games_played"]) > calculate_stats(playerTwo["total_rebound"], playerTwo["num_games_played"]):
        playerOne_advantage += 1
    else: 
        playerTwo_advantage += 1
    
    #The user must first see the player statistics of the two players
    print("\nBorgie: Get ready to witness the outstanding stats of two basketball players who define excellence on the court: \n")
    resp.view_statistics(playerOne)
    print("\n")
    resp.view_statistics(playerTwo)
    print("\n")

    #Borgie will create a conclusion base from the data he gathers.
    if(playerOne_advantage == playerTwo_advantage): #condition if both players have the same number of advantage
        print(resp.after_comp_response_equal_stats(playerOne["player_name"], playerTwo["player_name"]))
    else: #if there is atleast one that stands out        
        print(resp.after_comp_response_with_advantage(playerOne["player_name"], playerTwo["player_name"])) if playerOne_advantage > playerTwo_advantage else print(resp.after_comp_response_with_advantage(playerTwo["player_name"], playerOne["player_name"])
)

#if certain player not found, user must provide the data and will be save in json
def generate_player(player: dict):
    #load data again from the json file for specific purpose
    player_info: dict = load_data_stats('player_stats.json')

    #append the player in the json file when player doesn't exist yet 
    player_info["player_stats"].append(
        {"player_name": player["player_name"],
        "num_games_played": player["num_games_played"],
        "total_point": player["total_point"],
        "total_three_point": player["total_three_point"],
        "three_points_attempt": player["three_points_attempt"],
        "total_assist": player["total_assist"],
        "total_rebound": player["total_rebound"]})

    #save player info
    save_data_stats('player_stats.json', player_info)
