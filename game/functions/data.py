from game.data.base import dirs, files
from json import dump, load
from os.path import exists
from os import makedirs



# Helper functions #

def create_required():
    """
        Creates a directory at the specified path if it does not already exist.

        Args:
            path (str): The path where the directory should be created.
    """
    for dir in dirs:
        makedirs(dir, exist_ok=True)

def create_stats_file():
    """
        Creates a stats.json file in the settings directory if it does not already exist.
        The file is initialized with default statistics for the game.

        The default statistics include:
            - total_games: 0
            - player_wins: 0
            - ai_wins: 0
    """

    file = files[1]
    if not exists(file):
        json_data = {
            "total_games": 0,
            "player_wins": 0,
            "ai_wins": 0
        }
        with open(file, "w") as f:
            dump(json_data, f, indent=4)

# data functions #

def setup():
    """
        Sets up the required directories and files for the Tic-Tac-Toe-ML game.
        This function creates the necessary directories and file if they do not already exist.
    """

    create_required()
    create_stats_file()


def load_stats():
    """
        Loads the statistics from the stats.json file in the data directory.

        Returns:
            dict: A dictionary containing the loaded statistics.
    """

    file = files[1]
    with open(file, "r") as f:
        return load(f)


def save_stats(stats):
    """
        Saves the provided statistics to the stats.json file in the data directory.

        Args:
            stats (dict): A dictionary containing the statistics to be saved.
    """

    file = files[1]
    with open(file, "w") as f:
        dump(stats, f, indent=4)