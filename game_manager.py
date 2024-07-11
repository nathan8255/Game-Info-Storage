from game import Game
from database_functions import *
from colorama import just_fix_windows_console, Fore
from prettytable.colortable import ColorTable, Theme

class GameManager:
    def __init__(self):
        self.games = {
            #game id : game object
        }
    
    def initalizeGames(self):
        for id in getGames():
            self.games[id] = getGameInfo(id)
            self.games[id].tags = getTags(id)

    def createGame(self):
        name = input("Enter name of game: ")

        achievement = input("Enter achievement %: ")
        if (achievement.isdigit() == False): achievement = 0

        tags = []
        status = input("Enter completion status: ") 
        game = Game(name, achievement, status, tags)

        id = addGame(game)
        self.games[id] = game

        #append tags to game
        while True:
            enteredTag = input("Enter tag (\"STOP\" to stop entering tags): ")
            if (enteredTag == "STOP"): break
            if (enteredTag in tags):
                print("Duplicate tag recieved! All game tags should be unique.")
                continue
            tags.append(enteredTag)
            addTag(id, enteredTag)
            
        if (len(tags) == 0):
            tags.append("None")
            addTag(id, "None")
    
    def printGames(self):
        tableTheme = Theme(
        default_color=Fore.CYAN,
        vertical_color=Fore.BLUE,
        horizontal_color=Fore.RED,
        junction_color=Fore.WHITE,
        )
        table = ColorTable(theme=tableTheme)
        table.field_names = ["Name", "Tags", "Achievement", "Status"]

        for game in self.games.values():
            formatedTags = """"""
            for tag in game.tags:
                if (tag == game.tags[-1]):
                    formatedTags += f"{tag}"
                else:
                    formatedTags += f"{tag}, "
            table.add_row([game.name, formatedTags, f"{game.achievement}%", game.status])

        print(table)