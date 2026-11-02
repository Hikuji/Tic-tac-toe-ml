
import colorama
from time import sleep

import game.ai.core as ai
import game.data.base as data
import game.functions.game as game
import game.functions.display as display
from game.functions.data import setup, save_stats


def main():
    setup()

    check = 1

    while True:
        if check:
            mode = "WELCOME"
        else:
            mode = "MENU"

        error = 0
        symbol = ""
        ai_symbol = ""

        ## 0 - game result (-1 - ai lose, 1 - draw, 2 - ai win), 1 - game positions <--> 2 - ai move
        game_data = [0, [], []]

        board = data.Board()


        while True:
            match mode:
                case "WELCOME":
                    display.welcome()
                    check = 0
                    mode = "MENU"

                case "MENU":
                    while True:
                        display.menu()
                        if error == 1:
                            print(f"{colorama.Fore.RED}Invalid input. {colorama.Style.BRIGHT}Please choose a valid option (1-3).{colorama.Style.RESET_ALL}")
                            error = 0

                        try:
                            choice = int(input(">>> "))
                    
                            if choice not in range(1, 5):
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

                            case 4:
                                mode = "CONFIRM_EXIT"
                                break

                case "GAME":
                    display.flush_input()
                    symbol = game.get_symbol(error)

                    if symbol == "X":
                        ai_symbol = "O"
                        mode = "PLAYER"

                    else:
                        ai_symbol = "X"
                        mode = "AI"

                case "PLAYER":
                    display.clear()
                    print(f"{colorama.Style.BRIGHT}Your turn.{colorama.Style.RESET_ALL}")
                    display.board(board.schema)

                    while True:
                        try:
                            print("Enter your move. Choose a number from 1 to 9.")
                    
                            if error == 1 :
                                print(f"{colorama.Fore.RED}Invalid input. {colorama.Style.BRIGHT}Please enter a number between 1 and 9.{colorama.Style.RESET_ALL}")
                            elif error == 2:
                                print(f"{colorama.Fore.RED}Invalid moove. {colorama.Style.BRIGHT}Please choose an empty cell between 1 and 9.{colorama.Style.RESET_ALL}")
                            error = 0

                            display.flush_input()
                            move = int(input(">>> ")) - 1
                    
                            if move in (a for a in range(9)) and board.board[1][move] not in ["X", "O"]:
                                break
                    
                            else:
                                error = 2
                    
                        except ValueError:
                            error = 1

                    board.board[1][move] = symbol
                    board.board[0][move] = colorama.Style.BRIGHT + colorama.Fore.GREEN

                    status = game.check_board(board.board[1])

                    if status is not None:
                        if status[0] == "draw":
                            game_data[0] = 1
                        else:
                            game_data[0] = -1

                        mode = "END"
                        continue

                    mode = "AI"

                case "AI":
                    display.clear()
                    print(f"{colorama.Style.BRIGHT}AI turn.{colorama.Style.RESET_ALL}")
                    display.board(board.schema)

                    game_data[1].append(ai.convert(board.board[1]))

                    ai_move = ai.move(board.board[1])
                    game_data[2].append(ai_move)

                    board.board[1][ai_move] = ai_symbol
                    board.board[0][ai_move] = colorama.Style.BRIGHT + colorama.Fore.BLUE

                    for i in range(3):
                        print(".", end="", flush=True)
                        sleep(1)
                    print()

                    status = game.check_board(board.board[1])

                    if status is not None:
                        if status[0] == "draw":
                            game_data[0] = 1
                        else:
                            game_data[0] = 2 

                        mode = "END"
                        continue
                    
                    mode = "PLAYER"

                case "END":
                    ai.save_game(game_data, board.board[1])
                    save_stats(status[0], symbol)
                    game.color_board(board.board[0], status[1])
                    display.win(board.schema, status[0], symbol, data.settings["ai_name"])
                    break

                case "RULES":
                    display.rules()
                    mode = "MENU"

                case "STATS":
                    display.stats()
                    mode = "MENU"

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