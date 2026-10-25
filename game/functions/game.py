

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


def check_board(board):
    """
        Checks the current state of the game board to determine if there is a winner or if the game is a draw.

        Args:
            board (list): The game board.

        Returns:
            str: The result of the game. It can be 'X' if player X wins, 'O' if player O wins, 'Draw' if the game is a draw, or None if the game is still ongoing.
    """

    combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]

    if all(isinstance(cell, str) for cell in board):
        return "Draw"

    return None
