import random


def createBoard(sizeHor, sizeVert):
    board = []

    for x in range(0, sizeVert):
        board.append([])
        for y in range(0, sizeHor):
            board[x].append('.')

    return board


def showBoard(board):
    for row in board:
        print(' '.join(row))


def initPlayerPos(board, player):
    width = len(board[0])
    height = len(board)

    playerRow = random.randrange(0, width)
    playerCol = random.randrange(0, height)

    placePlayer(board, player, playerRow, playerCol)

    return board, player


def placePlayer(board, player, newX, newY):
    # clear old position
    board[player['col']][player['row']] = "."
    # assign new position
    player['col'] = newY
    player['row'] = newX
    board[newY][newX] = "@"
