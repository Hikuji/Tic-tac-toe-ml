from ..data import base
from json import load, dump
from random import randint as randomize


games = {}

# Helper functions #
def convert(board):
    """
        Converts the current game board list into a standardized string pattern.
        Replaces empty spaces with a dot ('.').

        Args:
            board (list): The current state of the board containing positions.

        Returns:
            str: A 9-character string representation of the board (e.g., "X...O...X").
    """

    converted_board = ""
    for i in board:
        if i in ["X", "O"]:
            converted_board += i

        else:
            converted_board += '.'

    return converted_board


def count_moves(position):
    """
        Counts the total number of turns/moves played on the board so far.
        Scans the board pattern string and increments for every non-dot character.

        Args:
            position (str): The current 9-character board representation.

        Returns:
            int: The total count of moves made in the current game.
    """
    count = 0
    for character in position:
        if character != ".":
            count += 1
    return count


def get_symmetries(patern, orig_move):
    """
        Generates all 8 unique symmetries for a given board pattern 
        and correctly tracks where the original move index lands in each symmetry.

        Args:
            patern (str): The 9-character board string.
            orig_move (int): The original move index (0-8).

        Returns:
            list: A list of tuples containing (symmetric_pattern, transformed_move_index).
    """
    rot90 = [6, 3, 0, 7, 4, 1, 8, 5, 2]
    flip_h = [2, 1, 0, 5, 4, 3, 8, 7, 6]

    symmetries = []
    current_p = patern
    current_move = orig_move

    for _ in range(4):
        if (current_p, current_move) not in symmetries:
            symmetries.append((current_p, current_move))
        
        f_p = "".join(current_p[flip_h[i]] for i in range(9))
        f_move = flip_h[current_move]
        if (f_p, f_move) not in symmetries:
            symmetries.append((f_p, f_move))
            
        current_p = "".join(current_p[rot90[i]] for i in range(9))
        current_move = rot90[current_move]
        
    return symmetries


def init():
    """
        Loads the AI's learned game patterns and weights from the JSON memory file into the global games dictionary.
    """
    global games

    with open(base.memory, "r") as f:
        games = load(f)


def save_to_file():
    """
        Saves the current state of the global games dictionary containing learned
        patterns and weights back to the JSON memory file with proper indentation.
    """
    with open(base.memory, "w") as f:
        dump(games, f, indent=4)


# main functions #
def move(board):
    """
        Calculates and returns the best available move index for the AI.
        Checks if the pattern exists in memory to exploit highest-rated moves,
        explores unknown moves, or initializes a new pattern if seen for the first time.

        Args:
            board (list): The current state of the board.

        Returns:
            int: The chosen board index (0-8) where the AI will place its symbol.
    """
    patern = convert(board)

    if patern in games:
        points = list(games[patern])
    
        while True:
            returning = 0
    
            if any(x > 0 for x in points):
                highest = -9999
                for i in range(9):
                    if points[i] > highest:
                        highest = points[i]
                returning = points.index(highest)
    
            elif any(x == 0 for x in points):
                while True:
                    idx = randomize(0, 8)
                    if points[idx] == 0:
                        returning = idx
                        break
    
            else:
                highest = -9999
                for i in range(9):
                    if points[i] > highest:
                        highest = points[i]
                returning = points.index(highest)
    
            if patern[returning] == ".":
                return returning
            else:
                points[returning] = -99999
    
    else:
        games[patern] = [0 for i in range(9)]
    
        while True:
            returning = randomize(0, 8)
    
            if patern[returning] == ".":
                return returning


def save_game(data, board):
    """
        Backpropagates and rewards/punishes the AI's move choices after a game ends.
        Applies a decay factor so that later moves receive stronger weights
        than early moves, reflecting their direct impact on the game outcome.
        Updates all 8 symmetrical configurations for accelerated learning.

        Args:
            data (list): A list containing game result, history of positions, and history of moves.
            board (list): The final state of the board.
    """
    result = data[0]
    positions = data[1]
    moves = data[2]

    if result == -1:
        base_points = -10
    elif result == 2:
        base_points = 10
    elif result == 1:
        base_points = 2
    else:
        base_points = 0

    decay = 0.7
    current_reward = base_points

    for i in reversed(range(len(moves))):
        orig_pattern = positions[i]
        orig_move = moves[i]

        all_variants = get_symmetries(orig_pattern, orig_move)

        for sym_pattern, transformed_move in all_variants:
            if sym_pattern not in games:
                games[sym_pattern] = [0.0 for _ in range(9)]
                
            games[sym_pattern][transformed_move] += current_reward
        
        current_reward *= decay

    save_to_file()
