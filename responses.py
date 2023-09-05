import ai_functions as func
import random

#display when player is not found
def player_unknown(name):
    print("\nBorgie: I'm sorry, but seems like \"" + name + "\" is not on my player database. In order for me know, can you kind provide me data by this certain player. Starting from the player name. ")

#response when comparing the two players have the same number of value in terms of there overall performance
def after_comp_response_equal_stats(playerOne: dict, playerTwo: dict):
    response = [
        "Borgie: To sum up our comparison between " + playerOne + " and " + playerTwo + ", we find that both players have the same overall performance with means to each of the records present. I can therefore conclude that they are really strong as player in their own right." ,
        "Borgie: So, after breaking down the performances, accolades, and playing records of " + playerOne + " and " + playerTwo + ", we see that both players have left an indelible mark as basketball players as they share the same number of advantages, solidifying their places among the basketball elite."
    ][random.randrange(2)]

    return response

#response when comparing the two players and there is one that standout
def after_comp_response_with_advantage(win_player: str, lose_player: str):
    response = [
        "Borgie: When we evaluate the career statistics of the two players, I can conclude that " + win_player + " is better than " + lose_player + " in their overall stats. Although it's apparent that each has had a remarkable impact when playing their games, it still differs in their own unique ways.",
        "Borgie: When it comes to the overall performance, " + win_player + " clearly outperforms " +  lose_player + ", consistently averaging more advantage performance throughout their careers.",
        "Borgie: As we can see, " + win_player + " has the advantage, having maintained a high level of performance and statistics than " + lose_player + ".",
        "Borgie: Base from the records I get " + win_player + " has a more impressive record more than " + lose_player + " which makes him dependable as teammate."
    ][random.randrange(4)]
    
    return response

#viewing of records
def view_statistics(player: dict):
    print("> Player Name: " + player["player_name"])
    print("> Number of Games Played: " + str(player["num_games_played"]))
    print("> Total Career Points: " + str(player["total_point"]))
    print("> Three Point Field Goal: " + str(player["total_three_point"]) + " out of " + str(player["three_points_attempt"]) + " attempts")
    print("> Assists Per Game: " + str(player["total_assist"]))
    print("> Rebounds Per Game: " + str(player["total_rebound"]))

#simple instruction
def instruction():
    print("In order for me to understand, here are the sample accepted keys that I will accept whenever you will ask me about the comparison of the two players:\n[/] Who is better, Lebron or Jordan?\n[/] Who is better between Lebron and Jordan?\n[/] Is Lebron better than Jordan?\nPlayers Jordan and Lebron are changeable, but format must be follow above. LASTLY, ONLY PROVIDE THE LAST OR FIRST NAME OF THE PLAYERS YOU WANT COMPARE BECAUSE I'M STILL NOT THAT INTELLIGENT.")

#response when user input invalid format
def invalid_input():
    response = [
        "Borgie: I'm sorry, but it seems like the input format you provided is not valid. Please make sure to follow the correct format so I can assist you better.",
        "Borgie: Oops! It looks like there's an issue with the format of your input. Could you please rephrase your request in a clear and structured manner?",
        "Borgie: I apologize, but I couldn't decipher your input because it doesn't adhere to the expected format. Please try again with a clear and well-structured query.",
        "Borgie: It seems there's a format error in your input. To assist you better, please provide the necessary information using the correct format or ask your question in a more straightforward manner."
    ][random.randrange(4)]
    
    return response




    