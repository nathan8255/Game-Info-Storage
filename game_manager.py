from game import Game

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
