Welcome to the Basketball Player Comparison project! This Python program allows you to compare the statistics of two basketball players. The comparison is based on various metrics such as total points, three-point field goals, assists, rebounds, and games played.

# Introduction
The project consists of three main modules:

1. **main.py**:
   This module contains the main functionality of the program. It prompts the user to input the names of two basketball players and then compares their statistics.

2. **ai_functions.py**:
   This module includes functions related to data handling and manipulation. It provides functions to load and save player data, find players in the database, generate new player records, and compare player statistics.

3. **responses.py**:
   This module contains response templates that the program uses to communicate with the user. It includes responses for various scenarios, such as when a player is not found, when comparing players with equal stats, and when one player has an advantage.

# How to Use
1. **Run the Program**: Execute `main.py` to start the program. Follow the instructions provided by Borgie to input the names of the players you want to compare.

2. **Input Player Information**: If the program doesn't recognize a player, it will prompt you to provide information about that player. You can choose to input the data or skip the step.

3. **Compare Players**: After providing the necessary information, Borgie will compare the two players and display the results.

4. **Quit**: If you want to exit the program, type 'quit' when prompted.

# File Structure

- `main.py`: Main program file for user interaction.
- `ai_functions.py`: Module containing functions for data manipulation.
- `responses.py`: Module with response templates for communication.
- `player_stats.json`: JSON file storing player statistics.
