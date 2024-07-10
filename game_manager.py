from game import Game
from colorama import just_fix_windows_console, Fore
from prettytable.colortable import ColorTable, Theme

class GameManager:
    def __init__(self):
        self.games = {
            #game name : game object
        }

    def createGame(self):
        name = input("Enter name of game: ")

        tags = []
        while True:
            enteredTag = input("Enter tag (\"STOP\" to stop entering tags): ")
            if (enteredTag == "STOP"): break
            if (enteredTag in tags):
                print("Duplicate tag recieved! All game tags should be unique.")
            tags.append(enteredTag)
        if (len(tags) == 0): tags.append("None")

        achievement = input("Enter achievement %: ")
        if (achievement.isdigit() == False): achievement = 0

        status = input("Enter completion status: ") 
        game = Game(name, tags, achievement, status)
        self.games[name] = game
        return game
    
    def printGames(self):
        tableTheme = Theme(
        default_color=Fore.CYAN,
        vertical_color=Fore.BLUE,
        horizontal_color=Fore.RED,
        junction_color=Fore.WHITE,
        )
        table = ColorTable(theme=tableTheme)
        table.field_names = ["Name", "Tags", "Achievement", "Status"]

        formatedTags = ""
        for game in self.games.values():
            for tag in game.tags:
                if (tag == game.tags[-1]):
                    formatedTags += f"{tag}"
                else:
                    formatedTags += f"{tag}, "
            table.add_row([game.name, formatedTags, f"{game.achievement}%", game.status])

        print(table)