from MyUtilities import clearScreen
from PlayerGenerator import *
from BoardGenerator import *


def getPlayerDirection():
    while True:
        inputDir = input("Which direction? (WASD): ").lower()
        # except:
        # print('Please enter W, A, S, or D.')

        for char in "w a s d".split():
            if inputDir == char:
                return inputDir
            else:
                continue
                print('Please input W, A, S, or D.')


def main():
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

    print("Please input board size preferences.")
    boardWidth = int(input("Width: "))
    boardHeight = int(input("Height: "))

    gameBoard = createBoard(boardWidth, boardHeight)
    initPlayerPos(gameBoard, you)
    clearScreen()
    showBoard(gameBoard)


main()
