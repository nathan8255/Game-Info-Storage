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
        tag1 = input("Enter first tag: ")
        tags = [tag1]
        tag2 = input("Enter second tag: ")
        tags.append(tag2)
        tag3 = input("Enter third tag: ")
        tags.append(tag3)
        achievement = input("Enter achievement %: ")
        status = input("Enter completion status: ") 
        game = Game(name, tags, achievement, status)
        self.games[name] = game
    
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
            formatedTags = f"{game.tags[0]}, {game.tags[1]}, {game.tags[2]}"
            table.add_row([game.name, formatedTags, "{game.achievement}%", game.status])

        print(table)