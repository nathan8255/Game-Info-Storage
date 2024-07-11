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
    dbCursor.execute(f"CREATE TABLE IF NOT EXISTS {TagsTable} (tag VARCHAR(255) PRIMARY KEY)")
    dbCursor.execute(f"CREATE TABLE IF NOT EXISTS {CombinationTable} (gameID INT NOT NULL, tag VARCHAR(255) NOT NULL, PRIMARY KEY(gameID, tag))")

def addGame(game):
    sql = f"INSERT INTO {GamesTable} (name, achievement, status) VALUES (%s, %s, %s)"
    values = (game.name, game.achievement, game.status)
    dbCursor.execute(sql, values)

    gameDB.commit()

    return dbCursor.lastrowid

def updateGame(id, game):
    sql = f"UPDATE {GamesTable} SET name = %s, achievement = %s, status = %s WHERE id={id}"
    values = (game.name, game.achievement, game.status)
    dbCursor.execute(sql, values)

    gameDB.commit()

def addTag(id, tag):
    dbCursor.execute(f"SELECT EXISTS(SELECT * FROM {TagsTable} WHERE tag=\"{tag}\")")
    existCheck = dbCursor.fetchall()
    if existCheck[0][0] == 0:
        sql = f"INSERT INTO {TagsTable} (tag) VALUES (%s)"
        values = [tag]
        dbCursor.execute(sql, values)

    sql = f"INSERT INTO {CombinationTable} (gameID, tag) VALUES (%s, %s)"
    values = (id, tag)
    dbCursor.execute(sql, values)
    
    gameDB.commit()

def getGames():
    dbCursor.execute(f"SELECT id FROM {GamesTable}")
    results = dbCursor.fetchall()

    output = []
    for id in results:
        output.append(id[0])
    return output

def getGameInfo(id):
    dbCursor.execute(f"SELECT name, achievement, status FROM {GamesTable} WHERE id={id}")
    results = dbCursor.fetchall()

    return Game(results[0][0], results[0][1], results[0][2])

def getTags(id):
    dbCursor.execute(f"SELECT t.tag FROM {GamesTable} g INNER JOIN {CombinationTable} c ON c.gameID = g.id INNER JOIN {TagsTable} t ON c.tag = t.tag WHERE g.id={id}")
    results = dbCursor.fetchall()

    output = []
    for tag in results:
        output.append(tag[0])
    return output