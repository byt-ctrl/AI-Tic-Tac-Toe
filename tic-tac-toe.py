# TIC-TAC-TOE GAME


import random
import time  # Adding delay for to think AI's move to feel little realistic

# Initializing an empty 3*3 board

game_board=[' ' for _ in range(9)]  # using '_' for ignored index

# Symbols for each player
human_symbol='X'
bot_symbol='O'
 

# Displaying the board
def display_board() :

    """displays the tic-tac-toe board."""
    
    for index in range(0,9,3) :

        print(f" {game_board[index]} | {game_board[index+1]} | {game_board[index+2]} ")

        if index<6 :
            print("---+---+---")  # For Proper alignment
    print("\n")  # extra line for better readability


# Checking if there is a winner

def check_victory(symbol) :

    """Checks if symbol 'X' or 'O' has won."""
    
    winning_combinations=[
                             (0,1,2), (3,4,5) , (6,7,8),                   # Rows
                             (0,3,6) , (1,4,7) , (2,5,8),                   # Column
                             (0,4,8) , (2,4,6)                               # Diagonals
                           ]
    
    # Possible win conditions
    for combinations in winning_combinations:
        if all(game_board[position]==symbol for position in combinations):  
            return True
    return False


# To get available moves

def get_moves():

    """List of available moves (i.e empty spaces)"""
    return [index for index in range(9) if game_board[index] == ' ']  




# Bot Turn (random move)

def bot_move():

    """Here Bot selects the random space."""

    time.sleep(1)  # Adding delay for to think Bot's move to feel little realistic
    return random.choice(get_moves())





# Human Turn (user input)

def human_move():

    """USER Input."""
    
    move = None  # Starting with invalid input to enter the loop
    while move not in get_moves():

        try:
            move = int(input("Enter your move (1-9) --> ")) - 1  # Doing '-1' because for 1 the index is 0
            if move not in get_moves():
                print("Invalid Move ! That spot is not available.")
        except ValueError:
            print("Please enter a number between 1-9 .")
    
    return move


# Main game loop

def play_game():
    print("Welcome to Tic-Tac-Toe Game !")
    display_board()  # showing empty board initially

    while True:
        # Human's turn
        human_choice = human_move()
        game_board[human_choice] = human_symbol
        display_board()

        if check_victory(human_symbol):
            print("Congratulations! You win! 🎉")    # You Win's
            break


        # Bot's turn
        print("Bot is thinking......\n")
        bot_choice = bot_move()
        game_board[bot_choice] = bot_symbol
        display_board()

        if check_victory(bot_symbol):
            print("Bot wins! Better luck next time . 🤖")    # Bot Win's
            break

        if not get_moves():  # if there are no moves available in the board
            print("It's a draw ! 🤝")
            break

# Calling function to start the game.
play_game()
