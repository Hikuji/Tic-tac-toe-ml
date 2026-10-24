

# Helper functions #



# Game functions #

def get_symbol():
    """
        Prompts the player to choose their symbol (X or O) and returns the chosen symbol in uppercase.

        Returns:
            str: The symbol chosen by the player, either 'X' or 'O'.
    """

    while True:
        symbol = input("Choose your symbol (X or O): ").upper()

        if symbol in ["X", "O"]:
            return symbol
        
        else:
            print("Invalid input. Please choose either X or O.")

def get_move(board):
    """
        Prompts the player to enter their move (a number between 1 and 9) and returns the corresponding index in the game board (a number between 0 and 8).

        Args:
            board (list): The game board.

        Returns:
            int: The index of the chosen move in the game board (a number between 0 and 8).
    """

    while True:
        try:
            move = int(input("Enter your move. Choose from 1 to 9: ")) - 1

            if move in range(9) and type(board[move]) == int:
                return move
            
            else:
                print("Invalid move. Please choose an empty cell between 1 and 9.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")