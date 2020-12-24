# import numpy as np
import math.floor as floor

# solve function
def solve(board):

    # count n empty tiles
    emptyTiles = 0
    for iRow in range(9):
        for jCol in range(9):
            if board[iRow][jCol] == 0:
                emptyTiles += 1

    # define n-by-9 boolean array
    isValid = [[True] * 9] * emptyTiles

    # while index < n
    kTile = 0
    pRow = 0
    qCol = 0
    while kTile < emptyTiles:

        # find empty tile
        isFound = False
        while ~isFound:
            if board[pRow][qCol] == 0:
                isFound = True
            qCol += 1
            if qCol == 9:
                pRow += 1
                qCol = 0

        # store invalid answers in corresponding row (ascending order)
        for sCol in range(9):
            if board[pRow][sCol] ~= 0:
                isValid[kTile][board[pRow][sCol] - 1] = False
        for rRow in range(9):
            if board[rRow][qCol] ~= 0:
                isValid[kTile][board[rRow][qCol] - 1] = False
        ## here goes the check for the local 3-by-3 square

        # if there are no valid answers:
            # index -= 1
            # if index = 0:
                # no solution
            # set tile to next valid answer and set corresponding boolean to 0
        # set empty tile to first valid answer and set corresponding boolean to 0
        # index += 1

# note: empty tiles contain 0

testBoard = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,8,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
solve(testBoard)