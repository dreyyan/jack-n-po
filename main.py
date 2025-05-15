 # # # # # # # # # # # # # # # # # # # # # # # #
#        Project: Rock, Paper, Scissors!        #
#         Author: dreyyan                       #
#       Language: Python                        #
#   Date Started: 05/15/2025                    #
#  Date Finished: 00/00/2025                    #
 # # # # # # # # # # # # # # # # # # # # # # # #
''' IMPORTS '''
import time, json, random, string, os, hashlib

''' MODULES '''
from modules.line_delay_animation import line_delay_animation
from modules.character_delay_animation import character_delay_animation
from modules.clear_screen import clear_screen
from modules.display_format import display_format
from modules.display_line import  display_line

''' UTILITIES '''
# UTILITY: Simulate a time delay within specified seconds
def delay(s):
    time.sleep(s)

# UTILITY: Display formatted error message to the user
def error_message(message):
    print(f"ERROR: {message}.")
    delay(2)

# UTILITY: Display header for the interface /w appropriate formatting
def display_header(interface_name, space, is_odd):
    line_delay_animation("[ Rock, Paper, Scissors! ]", 0.1)
    if is_odd:
        print(((space - 1) * '-'), end='') # Output spacing
    else:
        print((space * '-'), end='')  # Output spacing
    line_delay_animation(f" {interface_name} {(space * '-')}", 0.1)

# UTILITY: Display the function in the main menu
def display_function(index, function_name):
    line_delay_animation(f"[{index}] {function_name}", 0.1)

# UTILITY: Prompt the user to press the Enter key to continue
def press_enter_to_continue():
    user_input = input("Press 'Enter' to continue...")

def player_scores():
    global player_points
    player_points += 1
    print("You won the round!")
    delay(2)

def opponent_scores():
    global opponent_points
    opponent_points += 1
    print("You lost the round...")
    delay(2)

def determine_winner():
    modes = {1: 1, 2: 3, 3: 5}
    wins_needed = (modes[mode] // 2) + 1

    if player_points >= wins_needed:
        return "Player"
    elif player_points >= wins_needed:
        return "Opponent"
    else: return ""

''' MAIN '''
mode = 1, 1 # 1 = Easy - BO1, 2 = Medium - BO3, 3 = Hard - BO5
user_choice, player_picked, opponent_picked = None, None, None
player_points, opponent_points = 0, 0

# Prompt user to enter choice
while True:
    while True:
        clear_screen() # Clear console screen
        display_header("MAIN MENU", 8, True)
        display_function(1, "Start")
        display_function(2, "Change Mode")
        display_function(3, "Exit")
        display_line('-', 25)
        print()
        
        try:
            user_choice = int(input(">> ").strip())
            # ERROR: Invalid user choice
            if user_choice not in [1, 2, 3]:
                error_message("Invalid choice, please select numbers from 1-3")
            else: break
        except ValueError:
            error_message("Invalid choice, please select numbers from 1-3")

    # Start the game
    if user_choice == 1:
        # Display game settings
        clear_screen() # Clear console screen
        display_header("START GAME", 7, False)
        modes = {1: "BO3", 2: "BO5", 3: "BO7"}
        print(f"MODE: {modes[mode]}")
        display_line('-', 25)
        print()
        print("starting game...")
        delay(2)

        # Officially start the game
        while True:
            # Player chooses a hand
            while True:
                try:
                    clear_screen()
                    # Display current score
                    line_delay_animation(f"[         YOU: {player_points}        OPPONENT: {opponent_points}        ]", 0.1)
                    line_delay_animation("Choose: [ (1)Rock | (2)Paper | (3)Scissors ]", 0.1)
                    player_picked = int(input(">> ").strip())

                    # ERROR: Out-of-range choice
                    if player_picked not in range(1, 4):
                        error_message("Invalid choice, please try again")
                        delay(2)
                    else: break
                except ValueError:
                    error_message("Invalid choice, please try again")
                    delay(2)
            
            # Opponent chooses a hand [1 = rock, 2 = paper, 3 = scissors]
            opponent_picked = random.randint(1, 3)
            hands = {1: "rock", 2: "paper", 3: "scissors"}
            opponent_hand = hands[opponent_picked]

            # Display each side's hands
            print(f"     [YOU]: {hands[player_picked]}")
            print(f"[OPPONENT]: {opponent_hand}")
            delay(2)

            # Determine who wins the point
            # CASE 1: Tie
            if (player_picked == opponent_picked):
                print("It's a tie!")
                delay(2)
            # CASE 2: rock vs. paper
            elif (player_picked == 1 or opponent_picked == 1) and (player_picked == 2 or opponent_picked == 2):
                if player_picked == 2: player_scores()
                else: opponent_scores()
            # CASE 3: rock vs. scissors
            elif (player_picked == 1 or opponent_picked == 1) and (player_picked == 3 or opponent_picked == 3):
                if player_picked == 1: player_scores()
                else: opponent_scores()
            # CASE 4: paper vs. scissors
            elif (player_picked == 2 or opponent_picked == 2) and (player_picked == 3 or opponent_picked == 3):
                if player_picked == 3: player_scores()
                else: opponent_scores()

            # If winner is determined...
            if determine_winner() != "":    
                print("Game has ended...")
                delay(2)
                if player_points > opponent_points:
                    print("You won the game, congratulations!")
                else: print("You lost, better luck next time...")
                delay(2)
                player_points, opponent_points = 0, 0
                break

    # CHANGE Mode
    elif user_choice == 2:
        while True:
            clear_screen() # Clear console screen
            display_header("CHANGE MODE", 8, True)
            display_function(1, "BO3")
            display_function(2, "BO5")
            display_function(3, "BO7")
            display_line('-', 25)
            print()

            try:
                mode = int(input(">> ").strip())
                if mode not in [1, 2, 3]:
                    error_message("Invalid choice, please select numbers from 1-3")
                else: break
            except ValueError:
                error_message("Invalid choice, please select numbers from 0-2")

        # Display updated mode
        print("Mode set to '", end="")
        if mode == 1: # MODE: Best-of-3
            print("BO3", end="")
        elif mode == 2: # MODE: Best-of-5
            print("BO5", end="")
        elif mode == 3: # MODE: Best-of-7
            print("BO7", end="")
        print("'")
        delay(2)

    # EXIT Game
    elif user_choice == 3:
        print("Thank you for playing!")
        delay(2)
        exit(0)

    else:
        error_message("Invalid choice, please try again")