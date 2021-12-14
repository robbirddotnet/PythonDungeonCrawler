from PlayerGenerator import generateCharacter, displayHistory, displayStats
from BoardGenerator import createBoard, initPlayerPos, showBoard
from MyUtilities import clearScreen
from PlayerActions import commandPlayer
from TreasureGenerator import *
from Combat import *
import math


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

    clearScreen()
main()
