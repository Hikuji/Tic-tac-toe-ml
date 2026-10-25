from ..data.base import reset
from .data import load_stats
import colorama
import os

# Helper functions #



# display functions #

def clear():
    """
        Clears the console screen based on the operating system.
    """

    os.system("cls" if os.name == "nt" else "clear")


def line(multiplier = 80, style = colorama.Style.BRIGHT + colorama.Fore.BLACK):
    """
        Prints a horizontal line made of '=' characters with the specified style and length.
        If no arguments are provided, it defaults to a length of 80 characters and a black light style.

        Args:
            multiplier (int): The number of '=' characters to print in the line.
            style (str): The style for the line characters.
    """

    print(f"{style}={colorama.Style.RESET_ALL}" * multiplier)


def box(text, text_style = colorama.Style.BRIGHT + colorama.Fore.YELLOW, box_style = colorama.Style.BRIGHT + colorama.Fore.BLACK):
    """
        Displays a text inside a box made of '=' characters with the specified text and box styles.
        If no arguments are provided, it defaults to a yellow light text style and a black light box style.

        Args:
            text (str): The text to be displayed inside the box.
            text_style (str): The style for the text inside the box.
            box_style (str): The style for the box characters.
    """

    def empty_line():
        print(f"{box_style}={colorama.Style.RESET_ALL}", end="")
        print(" " * (len(text) + 2), end="")
        print(f"{box_style}={colorama.Style.RESET_ALL}")

    line(4 + len(text), box_style)
    empty_line()
    print(f"{box_style}={colorama.Style.RESET_ALL} {text_style}{text}{colorama.Style.RESET_ALL} {box_style}={colorama.Style.RESET_ALL}")
    empty_line()
    line(4 + len(text), box_style)

# Outputs #

def welcome():
    """
        Displays a welcome message for the Tic-Tac-Toe-ML game, explaining the game and prompting the player to start.
    """

    clear()
    box("Tic-Tac-Toe-ML", colorama.Style.BRIGHT + colorama.Fore.MAGENTA)
    line()
    print(f"Welcome to {colorama.Fore.MAGENTA + colorama.Style.BRIGHT}Tic-Tac-Toe-ML{colorama.Style.RESET_ALL}")
    print("Tic-tac-toe game using self-learning AI to play against you.")
    print("You can choose to play as X or O, and the AI will adapt to your playing style.")
    line()
    print(f"You can press {colorama.Fore.CYAN}Ctrl + C{colorama.Style.RESET_ALL} to open the settings menu at any time during the game.")
    print()
    input(f"Press {colorama.Fore.CYAN}Enter{colorama.Style.RESET_ALL} to start the game...")


def menu():
    """
        Displays the main menu for the Tic-Tac-Toe-ML game, allowing the player to choose between starting a game, viewing statistics, or exiting.
    """

    clear()
    box("Menu")
    line(40)
    print(f"{colorama.Fore.CYAN}Ctrl + C{colorama.Style.RESET_ALL}. Settings")
    print()
    print(f"{colorama.Fore.CYAN}1{colorama.Style.RESET_ALL}. Start Game")
    print(f"{colorama.Fore.CYAN}2{colorama.Style.RESET_ALL}. Statistics")
    print(f"{colorama.Fore.CYAN}3{colorama.Style.RESET_ALL}. Exit")
    line(40)
    print(f"You can press {colorama.Fore.CYAN}Ctrl + C{colorama.Style.RESET_ALL} to open the settings menu at any time during the game.")
    print(f"Choose an option by entering the corresponding number (1-3) or press {colorama.Fore.CYAN}Ctrl + C{colorama.Style.RESET_ALL} to open the settings menu.")
    print()


def stats():
    """
        Displays the statistics for the Tic-Tac-Toe-ML game, including total games played, player wins, and AI wins.
    """

    clear()
    box("Statistics")
    line()
    stats = load_stats()
    print(f"Total games played: {colorama.Fore.BLUE + colorama.Style.BRIGHT}{stats['total_games']}{colorama.Style.RESET_ALL}")
    print(f"Player wins: {colorama.Fore.GREEN + colorama.Style.BRIGHT}{stats['player_wins']}{colorama.Style.RESET_ALL}")
    print(f"AI wins: {colorama.Fore.RED + colorama.Style.BRIGHT}{stats['ai_wins']}{colorama.Style.RESET_ALL}")
    line()
    input(f"Press {colorama.Fore.CYAN}Enter{colorama.Style.RESET_ALL} to return to the menu...")


def exit_game():
    """
        Displays a farewell message.
    """

    clear()
    box("Goodbye!", colorama.Style.BRIGHT + colorama.Fore.RED)
    print("See you next time!")
    print()
    input(f"Press {colorama.Fore.CYAN}Enter{colorama.Style.RESET_ALL} to exit...")


def board(board):
    """
        Displays the current state of the game board.

        Args:
            board (list): The game board to be displayed.
    """
    print(reset, end="")
    for i in board:
        print(reset, end="")
        print(i)
    print()

def win(winner, player_symbol, name):
    """
        Displays a winning message if the player wins the game.

        Args:
            winner (str): The symbol of the winning player ('X' or 'O').
            player_symbol (str): The symbol of the player ('X' or 'O').
            name (str): The name of the AI.
    """

    line()
    if winner == player_symbol:
        print(f"{colorama.Fore.GREEN}Congratulations! You win as {winner}!{colorama.Style.RESET_ALL}")
    else:
        print(f"{colorama.Fore.RED}Game over! {name} ({winner}) wins!{colorama.Style.RESET_ALL}")
    line()