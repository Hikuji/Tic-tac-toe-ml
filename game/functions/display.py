import os

# Helper functions #

def clear():
    """
        Clears the console screen based on the operating system.
    """

    os.system("cls" if os.name == "nt" else "clear")

# Outputs #

def Hello_game():
    """
        Displays a welcome message for the Tic-Tac-Toe-ML game, explaining the game and prompting the player to start.
    """

    clear()
    print("=" * 30)
    print("Welcome to Tic-Tac-Toe-ML!")
    print("Tic-tac-toe game using self-learning AI to play against you.")
    print("You can choose to play as X or O, and the AI will adapt to your playing style.")
    print("=" * 30)
    print()
    input("Press Enter to start the game...")

def printBoard(board, reset):
    """
        Displays the current state of the game board.

        Args:
            board (list): The game board to be displayed.
            reset (str): The color reset code from colorama to reset the text color after displaying the board.
    """
    print(reset, end="")
    for i in board:
        print(reset, end="")
        print(i)
    print()

