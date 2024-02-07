from game_manager import GameManager
from colorama import just_fix_windows_console, Fore
import os

manager = GameManager()

def displayHelpInfo():
    print("--> NEW\nAdd a new game to track.\n")
    print("--> HELP\nDisplayes help info.\n")
    print("--> EXIT\nExit game manager.\n")

def parseSelection(command):
    os.system('cls')
    if (command == "NEW"):
        print()
    elif (command == "EXIT"):
        print()
    elif (command == "HELP"):
        displayHelpInfo()
    else:
        print("[Input was invalid, displaying \"HELP\" info.]\n")
        displayHelpInfo()