
import colorama

import game.data.base as data
import game.functions.game as game
import game.functions.display as display
from game.functions.data import setup


def main():
    ## 0 - game mode, 1 - error message##
    mode = "WELCOME"
    error = 0
    symbol = ""
    game_data = []

    board = data.Board()


    setup()

    while True:
        match mode:
            case "WELCOME":
                display.welcome()
                mode = "MENU"

            case "MENU":
                while True:
                    display.menu()
                    if error == 1:
                        print(f"{colorama.Fore.RED}Invalid input. {colorama.Style.BRIGHT}Please choose a valid option (1-3).{colorama.Style.RESET_ALL}")
                        error = 0

                    try:
                        choice = int(input(">>> "))
                
                        if choice not in range(1, 6):
                            raise ValueError
                
                    except ValueError:
                        error = 1
                        continue

                    match choice:
                        case 1:
                            mode = "GAME"
                            break

                        case 2:
                            mode = "RULES"
                            break

                        case 3:
                            mode = "STATS"
                            break

                        case 5:
                            mode = "CONFIRM_EXIT"
                            break

            case "GAME":
                display.clear()
                symbol = game.get_symbol(error)

                if symbol == "X":
                    mode = "PLAYER"

                else:
                    mode = "AI"

            case "PLAYER":
                display.clear()
                print(f"{colorama.Style.BRIGHT}Your turn.{colorama.Style.RESET_ALL}")
                move = game.get_move(board.board[1], error)
                board.board[1][move] = symbol

                status = game.check_board(board.board[1])

                if status == symbol:
                    mode = "WIN - PLAYER"
                    continue

                elif status == "draw":
                    mode = "DRAW"
                    continue

                mode = "AI"

            case "AI":
                pass

            case "RULES":
                display.rules()
                mode = "MENU"

            case "STATS":
                display.stats()
                mode = "MENU"

            case "SETTINGS":
                pass

            case "CONFIRM_EXIT":
                display.confirm_exit()
                answer = input(">>> ")

                if answer == 'Y':
                    mode = "EXIT"

                elif answer in ("N", "n"):
                    mode = "MENU"

            case "EXIT":
                display.exit_game()
                quit()
                
        

            
    
if __name__ == "__main__":
    main()