import game.data.base as base
from json import dump, load
from os.path import exists
from os import makedirs
from ..ai.core import init



# Helper functions #

def create_required():
    """
        Creates a directory at the specified path if it does not already exist.

        Args:
            path (str): The path where the directory should be created.
    """
    for dir in base.dirs:
        makedirs(dir, exist_ok=True)

def create_stats_file():
    """
        Creates a stats.json file in the settings directory if it does not already exist.
        The file is initialized with default base.statistics for the game.

        The default base.statistics include:
            - total_games: 0
            - player_wins: 0
            - ai_wins: 0
            - draws: 0
    """

    file = base.files[1]
    if not exists(file):
        json_data = {
            "total_games": 0,
            "player_wins": 0,
            "ai_wins": 0,
            "draws": 0
        }
        with open(file, "w") as f:
            dump(json_data, f, indent=4)


def create_settings_file():
    """
        Creates a settings.json file in the settings directory if it does not already exist.
        The file is initialized with default settings for the game.
    
        The default setttings include:
            - board_numbering: True
    """
    
    file = base.files[0]
    if not exists(file):
        json_data = {
            "board_numbering": True,
            "ai_name": "AI"
        }
        with open(file, "w") as f:
            dump(json_data, f, indent=4)


def create_memory_file():
    """
        Creates a memory.json file in the memory directory if it does not already exist.
    """

    file = base.files[2]
    if not exists(file):
        json_data = {}
        with open(file, "w") as f:
            dump(json_data, f, indent=4)


def get_settings():

    with open(base.files[0], "r") as f:
        base.settings = load(f)


def save_settings(settings):
    with open(base.files[0], "w") as f:
        dump(settings, f, indent=4)


# data functions #

def setup():
    """
        Sets up the required directories and files for the Tic-Tac-Toe-ML game.
        This function creates the necessary directories and file if they do not already exist.
    """

    create_required()
    create_stats_file()
    create_settings_file()
    create_memory_file()
    init()
    load_stats()
    get_settings()


def load_stats():
    """
        Loads the base.statistics from the stats.json file in the data directory.

        Returns:
            dict: A dictionary containing the loaded base.statistics.
    """

    with open(base.files[1], "r") as f:
        base.statistics = load(f)


def save_stats(result, player):
    """
        Saves the provided base.statistics to the stats.json file in the data directory.

        Args:
            stats (dict): A dictionary containing the base.statistics to be saved.
    """

    if result == player:
        base.statistics["player_wins"] += 1

    elif result == "draw":
        base.statistics["draws"] += 1

    else:
        base.statistics["ai_wins"] += 1

    base.statistics["total_games"] += 1

    with open(base.files[1], "w") as f:
        dump(base.statistics, f, indent=4)