import enum

class Game:
  def __init__(self, name, tags, achievement, status):
    self.name = name
    self.tags = tags
    self.achievement = achievement
    self.status = status

  def __str__(self):
    return f"{self.name}"
  
class Tag(enum.Enum):
  Card = 1
  Difficult = 2
  Horror = 3

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
print(game)