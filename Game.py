from MyUtilities import clearScreen
from PlayerGenerator import *
from BoardGenerator import *


def getPlayerDirection():
    while True:
        inputDir = input("Which direction? (WASD): ").lower()

        for char in "w a s d".split():
            if inputDir == char:
                return inputDir
            else:
                continue
                print('Please input W, A, S, or D.')


def calcNewCoords(dir, currentX, currentY):
    # calculate move direction
    # vertical movement is logically inverted
    if dir == 'w':  # up
        newX = currentX
        newY = currentY - 1
    elif dir == 's':  # down
        newX = currentX
        newY = currentY + 1
    elif dir == 'd':  # right
        newX = currentX + 1
        newY = currentY
    elif dir == 'a':  # left
        newX = currentX - 1
        newY = currentY

    return newX, newY


def commandPlayer(board, player):
    while True:
        clearScreen()
        showBoard(board)
        inputDir = getPlayerDirection()

        newX, newY = calcNewCoords(inputDir, player['row'], player['col'])

        width = len(board[0]) - 1
        height = len(board) - 1

        if newX < 0 or newX > width or newY < 0 or newY > height:
            # Invalid direction. Out of bounds.
            continue

        # update new player location on the board to a "@"
        placePlayer(board, player, newX, newY)

    return board, player


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

    while True:
        commandPlayer(gameBoard, you)


main()
