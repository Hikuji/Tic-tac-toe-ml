import colorama
import signal

import game.functions.display as display
from game.functions.data import setup

## 0 - game mode, 1 - can open settings, 2 - run settings 3 - error message ##
mode_cache = ["WELCOME", True, False, False]
# signal.signal(signal.SIGINT, )


def main():
    global mode_cache

    setup()

    while True:
        if mode_cache[0] == "WELCOME":
            display.welcome()
            mode_cache[0:2] = "MENU", True

        elif mode_cache[0] == "MENU":
            while True:
                display.menu()
                if mode_cache[3]:
                    print(f"{colorama.Fore.RED}Invalid input. {colorama.Style.BRIGHT}Please choose a valid option (1-3).{colorama.Style.RESET_ALL}")
                    mode_cache[3] = False

                try:
                    choice = int(input(">>> "))
            
                    if choice not in [1, 2, 3]:
                        raise ValueError
            
                except ValueError:
                    mode_cache[3] = True
                    continue

                if choice == 1:
                    mode_cache[0:2] = "GAME", True
                    break

                elif choice == 2:
                    mode_cache[0:2]  = "STATS", True
                    break

                elif choice == 3:
                    mode_cache[0:2] = "EXIT", False
                    break

        elif mode_cache[0] == "GAME":
            pass

        elif mode_cache[0] == "STATS":
            display.stats()
            mode_cache[0:2] = "MENU", True

        elif mode_cache[0] == "EXIT":
            display.exit_game()
            exit()
        

            
    
if __name__ == "__main__":
    main()