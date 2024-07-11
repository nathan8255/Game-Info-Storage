from game_manager import GameManager
from colorama import just_fix_windows_console, Fore
import os

manager = GameManager()

def displayHelpInfo():
    print("--> NEW\nAdd a new game to track.\n")
    print("--> EDIT\nModify information for a tracked game.\n")
    print("--> DISPLAY\nDisplays all added games.\n")
    print("--> HELP\nDisplayes help info.\n")
    print("--> HELP\nChange program settings.\n")
    print("--> EXIT\nExit game manager.")

def parseSelection(command):
    os.system('cls')
    if (command == "NEW"):
        manager.createGame()
    elif(command == "EDIT"):
        print(Fore.RESET)
        manager.printAllGames()
        print(Fore.CYAN)
        manager.editGame()
    elif(command == "DISPLAY"):
        print(Fore.RESET)
        manager.printAllGames()
        print(Fore.CYAN)
    elif (command == "HELP"):
        displayHelpInfo()
    elif (command == "SETTINGS"):
        print()
    elif (command == "EXIT"):
        exit()
    else:
        print("[Input was invalid, displaying \"HELP\" info.]\n")
        displayHelpInfo()

def setupManager():
    manager.initalizeGames()