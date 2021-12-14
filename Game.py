from PlayerGenerator import generateCharacter, displayHistory, displayStats
from BoardGenerator import createBoard, initPlayerPos, showBoard
from MyUtilities import clearScreen
from PlayerActions import commandPlayer
from TreasureGenerator import *
from Combat import *
import math
import collections

def checkWinState(player):
    # print("Checking winsate")
    if player['level'] >= 20:
        print("PLayer should win")
        return True
    else:
        print("Game should continue")
        return False


def showWinScreen():
    print("You win!")


def showGameOver():
    print("Game over!")


def endOfGameStats(player):
    # Print out the player's stats and achievements.
    print(player["name"] + " achieved level " + str(player["level"]))
    displayStats(player)
    # If no treasures were found, this will not run.
    if len(player["treasuresFound"]) > 0:
        print("Major Treasures unlocked: ")
        for item in player["treasuresFound"]:
            print(" * " + str(item))
    # If no enemies were killed, this will not run.
    if len(player["enemiesKilled"]) > 0:
        print("Enemies defeated: ")
        enemyList = collections.Counter(player["enemiesKilled"])
        # print(enemyList)
        for enemy in enemyList:
            print(str(enemy) + ": " + str(enemyList[enemy]))


def main():
    # Create a character and ask if it is desired.
    # if the player likes it, continue. Otherwise make a new one.
    # After that we enter the main game loop.
    while True:
        clearScreen()
        you = generateCharacter(1)
        displayHistory(you)
        print('\n')
        displayStats(you)

        response = input('\nDo you like this character? (y/n): ')

        if response.lower() == 'n':
            continue
        elif response.lower() == 'y':
            break
            clearScreen()

    # print("Please input board size preferences.")
    # boardWidth = int(input("Width: "))
    # boardHeight = int(input("Height: "))
    boardWidth = 10
    boardHeight = 10

    gameBoard = createBoard(boardWidth, boardHeight)
    initPlayerPos(gameBoard, you)
    greaterTreasures = []

    numTreasures = math.floor((boardWidth + boardHeight) / 3 + 1)
    print(numTreasures)
    # while numTreasures > 0:
    genTreasure(gameBoard, greaterTreasures, numTreasures)
    # placeTreasure(boardWidth, boardHeight, treasureName, treasureList)

    # gameplay loop
    awardMinorTreasure = False
    win = False

    while True:
        clearScreen()
        showBoard(gameBoard)
        if awardMinorTreasure:
            minorTreasure(you)

        checkTreasure(you, greaterTreasures, gameBoard)

        awardMinorTreasure = False
        minorRoll = commandPlayer(gameBoard, you)
        if minorRoll == 1:
            # print("Combat loop started.")
            playerMaxHP = you["Health"]
            enemy = createEnemy(you)
            if not combatLoop(you, enemy):
                break
            you["Health"] = playerMaxHP

        elif minorRoll == 6:
            awardMinorTreasure = True

        win = checkWinState(you)
        if win:
            break

    clearScreen()
    if win:
        showWinScreen()
    else:
        showGameOver()

    endOfGameStats(you)

main()
