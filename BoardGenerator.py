def createBoard():
    board = []

    for x in range(0, 5):
        board.append([])
        for y in range(0, 5):
            board[x].append('.')

    return board


def showBoard(board):
    for row in board:
        print(''.join(row))
