

# Helper functions #
def convert(board):
    """
    """

    converted_board = ""
    for i in board:
        if i in ["X", "O"]:
            converted_board += i

        else:
            converted_board += '.'

    return converted_board


def find():
    pass # search for game position


def save_game():
    pass


# main functions #
games = {}

def init():
    pass # get games data


def move():
    pass #chooses a move