from game import Game
from database_functions import *
from colorama import just_fix_windows_console, Fore
from prettytable.colortable import ColorTable, Theme
from colorama import just_fix_windows_console, Fore
import os

class GameManager:
    def __init__(self):
        self.games = {
            #game id : game object
        }
        self.achievementLimit = 100
    
    def initalizeGames(self):
        for id in getGames():
            self.games[id] = getGameInfo(id)
            self.games[id].tags = getTags(id)

    def formatTable(self):
        tableTheme = Theme(
        default_color=Fore.CYAN,
        vertical_color=Fore.BLUE,
        horizontal_color=Fore.RED,
        junction_color=Fore.WHITE,
        )
        table = ColorTable(theme=tableTheme)
        table.field_names = ["ID", "Name", "Tags", "Achievement", "Status"]
        return table

    def formatTags(self, game):
        formatedTags = """"""
        for tag in game.tags:
            if (tag == game.tags[-1]):
                formatedTags += f"{tag}"
            else:
                formatedTags += f"{tag}, "
        return formatedTags

    def createGame(self):
        name = input("Enter name of game: ")

        achievement = input("Enter achievement %: ")
        if (achievement.isdigit() == False): achievement = 0
        elif (int(achievement) < 0): achievement = 0
        elif (int(achievement) > self.achievementLimit): achievement = self.achievementLimit

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
    
    def editGame(self):  
        enteredID = 1
        while True:
            enteredID = int(input("Enter id to edit a game (\"RETURN\" to return to the menu): "))
            if (enteredID == "RETURN"): return
            if enteredID not in self.games.keys():
                print("Invalid ID recieved! Please enter the ID of one of the available games.")
                continue
            break

        while True:
            os.system("cls")
            print(Fore.RESET)
            self.printGame(enteredID)
            print(Fore.CYAN)
            column = input("Enter which column you would like to edit (\"RETURN\" to return to the menu): ")
            if (column == "RETURN"): break
            elif (column == "Name"):
                name = input("Enter a new name: ")
                self.games[enteredID].name = name
                updateGame(enteredID, self.games[enteredID])
            elif (column == "Tags"):
                print()
            elif (column == "Achievement"):
                print()
            elif (column == "Status"):
                status = input("Enter a new status: ")
                self.games[enteredID].status = status
                updateGame(enteredID, self.games[enteredID])
                print()
            else:
                print("Invalid column recieved! Please enter the name of a column other than \"ID\".")
                continue

    def printGame(self, id):
        table = self.formatTable()
        formatedTags = self.formatTags(self.games[id])
        table.add_row([id, self.games[id].name, formatedTags, self.games[id].name, self.games[id].status])
        print(table)

    def printGameList(self, games):
        table = self.formatTable()

        for id, game in games.items():
            formatedTags = self.formatTags(game)
            table.add_row([id, game.name, formatedTags, f"{game.achievement}%", game.status])

        print(table)

    def printAllGames(self):
        self.printGameList(self.games)
    