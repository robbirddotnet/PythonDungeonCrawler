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
        print(''.join(row))


def placePlayer(board, player):
    width = len(board[0])
    height = len(board)

    playerRow = random.randrange(0, width)
    playerCol = random.randrange(0, height)

    player['row'] = playerRow
    player['col'] = playerCol

    board[playerRow][playerCol] = "@"

    return board, player
