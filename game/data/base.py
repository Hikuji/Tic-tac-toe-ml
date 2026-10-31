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

        self.inschema = [
            f"{self.board[0][i]}{self.board[1][i]}{reset}" for i in range(9)
        ]

        self.schema = [
            "+-------+-------+-------+",
            "|       |       |       |",
            f"|   {self.inschema[0]}   |   {self.inschema[1]}   |   {self.inschema[2]}   |",
            "|       |       |       |",
            "+-------+-------+-------+",
            "|       |       |       |",
            f"|   {self.inschema[3]}   |   {self.inschema[4]}   |   {self.inschema[5]}   |",
            "|       |       |       |",
            "+-------+-------+-------+",
            "|       |       |       |",
            f"|   {self.inschema[6]}   |   {self.inschema[7]}   |   {self.inschema[8]}   |",
            "|       |       |       |",
            "+-------+-------+-------+"
        ]