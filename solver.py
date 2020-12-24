import numpy as np
import math
import time

def solve(board):

    # initialization of variables
    emptyTiles = 0
    coords = []
    kTile = 0

    # empty tiles count and coordinates storage
    for iRow in range(9):
        for jCol in range(9):
            if board[iRow , jCol] == 0:
                emptyTiles += 1
                coords.append([iRow , jCol])
    coords = np.array(coords)

    # boolean array containing valid answers for each empty tile
    isValid = np.array([[True] * 9] * emptyTiles)

    # board filling cycle
    while kTile < emptyTiles:

        # initialization of variables
        pRow = coords[kTile , 0]
        qCol = coords[kTile , 1]
        quad = [math.floor(pRow/3) * 3,
                math.floor(qCol/3) * 3] # 3-by-3 square location
        
        # resetting of discarded value when it's any but the last tile
        if kTile != emptyTiles - 1:
            isValid[kTile + 1] = [True] * 9
            board[coords[kTile + 1 , 0] , coords[kTile + 1 , 1]] = 0

        # valid answers checkup
        for sCol in range(9):
            if board[pRow , sCol] != 0:
                isValid[kTile , board[pRow][sCol] - 1] = False
        for rRow in range(9):
            if board[rRow , qCol] != 0:
                isValid[kTile , board[rRow][qCol] - 1] = False
        for tRow in range(quad[0] , quad[0] + 3):
            for uCol in range(quad[1] , quad[1] + 3):
                if board[tRow , uCol] != 0:
                    isValid[kTile , board[tRow][uCol] - 1] = False
        
        # return to previous tile when the program runs out of valid anwsers
        if np.sum(isValid[kTile]) == 0:
            if kTile != 0:
                kTile -= 1
            # no solution
            elif kTile == 0:
                print("No solution exists.")
                return 0
        # set current tile to next valid answer
        else:
            for vNum in range(9):
                if isValid[kTile , vNum]:
                    board[pRow , qCol] = vNum + 1
                    isValid[kTile , vNum] = False
                    print(board)
                    break
            kTile += 1
    
    # solution!
    return board

# NOTE: empty tiles contain 0
testBoard = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
])

solve(testBoard)