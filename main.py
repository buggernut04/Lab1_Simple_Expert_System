import re
import ai_functions as func
import responses as resp

# create function to minimize redundancy
# function to input the records of the player 
# helper function for input_stats
def points_getter(category) -> int:
    
    print("Borgie: Next will be the total " + category + " made.")
    
    while True:
        try:
            num = int(input("You: "))
            
            # it will not accept a stat with the value of 0
            if num <= 0:
                raise ValueError("Input must be a positive integer")
            break

        except ValueError:
            print("Borgie: Your input is invalid. Please input in numerical form and must be greater than zero.")
    
    return num

# inputting the stats if player doesn't exist
def input_stats() -> dict:
    # this is usefor user that inputted an existed player in the system.
    existing_players: dict = func.load_data_stats('player_stats.json')

    # the player name is the main basis to avoid duplicates
    # and that is this checker do
    while True:
        player_exists = False
        player_name = input("You: ")
         
        for player_record in existing_players["player_stats"]:
            player = player_name
            if player.lower() == player_record["player_name"].lower():
                player_exists = True
                break
        
        if player_exists:
            print("Borgie: Oopss! Seems like " + player_name + " already exists. Provide me another player information.")
        else: break
 
    total_points = points_getter("points")
    total_three_points = points_getter("three points")
    total_three_point_attempt = points_getter("three point attempts")
    total_assists = points_getter("assists")
    total_rebounds = points_getter("rebounds")
    total_games = points_getter("games")

    player_info = {
        "player_name": player_name,
        "num_games_played": total_games,
        "total_point": total_points,
        "total_three_point": total_three_points,
        "three_points_attempt": total_three_point_attempt,
        "total_assist": total_assists,
        "total_rebound": total_rebounds
    }

    return player_info

if __name__ == '__main__':
    #Last to implement is if both players have the same name.

    print("\nBorgie: Hey there, sport! I'm Borgie, your go-to basketball player comparison expert. Whether you're debating LeBron vs. Jordan, Curry vs. Harden, or any other basketball superstar showdown, I'm here to break it down for you. Just drop the names of the two basketball players you want to compare, and I'll serve up and compare them through their stats.\n")

    resp.instruction()

    print("\n* Kindly press 'quit' if you don't want me anymore.\n\nBorgie: Let's get the ball rolling who's on your court today?\n")

    # Define a list of regex patterns
    patterns = [
        r"Who is better, (\w+) or (\w+)\?",
        r"Who is better between (\w+) and (\w+)\?",
        r"Is (\w+) better than (\w+)\?"
    ]
   
    while True:
        player_input = input("You: ").strip().lower()

        if player_input.lower() == "quit":
            break

        has_match = False

        # Try each pattern until a match is found
        for pattern in patterns:
            match = re.search(pattern.strip().lower(), player_input)
            if match:
                has_match = True
                break  # Exit the loop if a match is found

        if has_match:
            #find the first player
            playerOne_stats: dict = func.find_player(match.group(1))
            
            #if certain player doesn't exist, it will generate one by providing info by the user
            if playerOne_stats == None:
                resp.player_unknown(match.group(1))

                #inputting player one stats
                playerOne_stats = input_stats()
                print("\nBorgie: Thank you for providing this information. I will add this to my system.")

                #generate player if there is no wrong with the input
                func.generate_player(playerOne_stats)
                #It is ensured that the player is already existed in the system
                playerOne_stats = func.find_player(playerOne_stats["player_name"])
            
            #find the second player
            playerTwo_stats: dict = func.find_player(match.group(2))
            
            #if certain player doesn't exist, it will generate one by providing info by the user
            if playerTwo_stats == None:
                resp.player_unknown(match.group(2))
                
                #inputting player two stats
                playerTwo_stats = input_stats()
                print("\nBorgie: Thank you for providing this information. I will add this to my system.")

                #generate player if there is no wrong with the input
                func.generate_player(playerTwo_stats)
                #It is ensured that the player is already existed in the system
                playerTwo_stats = func.find_player(playerTwo_stats["player_name"])

            # it will not going to compare if the same players are being compared
            if playerOne_stats["player_name"] == playerTwo_stats["player_name"]:
                print("\nBorgie: It appears that both players have the same name. To provide an accurate comparison, I need distinct names for the players. Only specify the last name if they have the same first name, and vice versa. I'll be happy to assist you further. ")
                continue
            #compare both players base from the information it contains
            else:
                func.compare_players(playerOne_stats, playerTwo_stats)
        else:
            print("\n" + resp.invalid_input())
            resp.instruction() 
            continue
    
        print("\nBorgie: Feel free to ask again. I'll be 24 hours in touch. Just type 'quit' if you don't want me anymore.\n")
