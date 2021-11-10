from MyUtilities import clearScreen
from PlayerGenerator import *
from BoardGenerator import *


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
