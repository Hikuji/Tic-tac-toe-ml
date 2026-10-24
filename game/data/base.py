from colorama import Fore, Style

reset = Fore.WHITE + Style.BRIGHT

board = [
    [
        Fore.YELLOW for i in range(9)
    ],
    [
        f"{i + 1}" for i in range(9)
    ]
]

inschema = [
    f"{board[0][i]}{board[1][i]}{reset}" for i in range(9)
]

schema = [
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