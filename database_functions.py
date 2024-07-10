from game import Game
import mysql.connector

#database setup
gameDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="no"
)

dbCursor = gameDB.cursor()

#database constants
DatabaseName = "GameInfoStorage"
GamesTable = "Games"
TagsTable = "Tags"
CombinationTable = "Games_Tags"
    
def setupDatabase():
    dbCursor.execute(f"CREATE DATABASE IF NOT EXISTS {DatabaseName}")
    gameDB.database = DatabaseName

    dbCursor.execute(f"CREATE TABLE IF NOT EXISTS {GamesTable} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), achievement INT, status VARCHAR(255))")
    dbCursor.execute(f"CREATE TABLE IF NOT EXISTS {TagsTable} (id INT AUTO_INCREMENT PRIMARY KEY, tag VARCHAR(255))")
    dbCursor.execute(f"CREATE TABLE IF NOT EXISTS {CombinationTable} (gameID INT NOT NULL, tagID INT NOT NULL, PRIMARY KEY(gameID, tagID))")

def addGame(game):
    sql = f"INSERT INTO {GamesTable} (name, achievement, status) VALUES (%s, %s, %s)"
    values = (game.name, game.achievement, game.status)

    dbCursor.execute(sql, values)
    gameDB.commit()

def addTag(tag):
    print()

def getGames():
    print()