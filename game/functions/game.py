from .display import clear
import colorama


# Helper functions #



# Game functions #

def get_symbol(error):
    """
        Prompts the player to choose their symbol (X or O) and returns the chosen symbol in uppercase.

        Returns:
            str: The symbol chosen by the player, either 'X' or 'O'.
            error (int): error hendler
    """

    while True:
        clear()
        print(f"Choose your symbol ({colorama.Style.BRIGHT}X{colorama.Style.RESET_ALL} or {colorama.Style.BRIGHT}O{colorama.Style.RESET_ALL})")

        if error == 1:
            print(f"{colorama.Fore.RED}Invalid input. {colorama.Style.BRIGHT}Please choose either X or O.{colorama.Style.RESET_ALL}")
        error = 0

        symbol = input(">>> ").upper()

        if symbol in ["X", "O"]:
            return symbol
        
        else:
            error = 1


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
            return (board[combo[0]], combo)

    if all(cell in ("X", "O") for cell in board):
        return ("draw", None)

    return None


def color_board(board_colors, combo):
    if combo is None:
        return
    else:
        for com in combo:
            board_colors[com] = colorama.Fore.RED