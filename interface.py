from input_functions import *
from database_functions import *
from colorama import just_fix_windows_console, Fore

#initial database setup
setupDatabase()
setupManager()

#initial interface setup
print(Fore.BLUE + "Game Manager")
status = "RUNNING"

#interface loop
while status != "EXIT":
    command = input(Fore.CYAN + "\nEnter Command: ")
    parseSelection(command)