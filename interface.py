from game_manager import GameManager
from input_functions import *
from database_functions import *
from colorama import just_fix_windows_console, Fore

manager = GameManager()

#initial database setup
setupDatabase()
manager.initalizeGames()

#initial interface setup
print(Fore.BLUE + "Game Manager")
status = "RUNNING"

#interface loop
while status != "EXIT":
    command = input(Fore.CYAN + "Enter Command: ")
    parseSelection(command)