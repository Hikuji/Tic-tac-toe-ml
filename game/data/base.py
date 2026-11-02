from colorama import Fore, Style
from platformdirs import user_data_dir


data_dir = user_data_dir("TicTacToeML", "Hikuji")
settings_dir = data_dir + "/settings"
ai_memory_dir = data_dir + "/ai_memory"

settings_file = settings_dir + "/settings.json"
stats_file = data_dir + "/stats.json"
memory = ai_memory_dir + "/memory.json"

dirs = [settings_dir, ai_memory_dir]
files = [settings_file, stats_file, memory]


reset = Fore.WHITE + Style.BRIGHT


settings = {}
statistics = {}


class Board:
    def __init__(self):
        self.board = [
            [
                Fore.YELLOW for i in range(9)
            ],
            [
                f"{i + 1}" for i in range(9)
            ]
        ]

    @property
    def schema(self):
        inschema = [
            f"{self.board[0][i]}{self.board[1][i]}{reset}" for i in range(9)
        ]

        return [
            "+-------+-------+-------+",
            "|       |       |       |",
            f"|   {inschema[0]}   |   {inschema[1]}   |   {inschema[2]}   |",
            "|       |       |       |",
            "+-------+-------+-------+",
            "|       |       |       |",
            f"|   {inschema[3]}   |   {inschema[4]}   |   {inschema[5]}   |",
            "|       |       |       |",
            "+-------+-------+-------+",
            "|       |       |       |",
            f"|   {inschema[6]}   |   {inschema[7]}   |   {inschema[8]}   |",
            "|       |       |       |",
            "+-------+-------+-------+"
        ]