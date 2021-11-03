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
