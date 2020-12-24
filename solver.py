import numpy as np
import math
import time

# solve function
def solve(board):

    # count n empty tiles and store coordinates
    solution = board
    emptyTiles = 0
    coords = []
    for iRow in range(9):
        for jCol in range(9):
            if board[iRow , jCol] == 0:
                emptyTiles += 1
                coords.append([iRow , jCol])
    coords = np.array(coords) # converted to numpy array for standardization

    # define n-by-9 boolean array
    isValid = np.array([[True] * 9] * emptyTiles)

    # while index < n
    kTile = 0
    while kTile < emptyTiles:
        pRow = coords[kTile , 0]
        qCol = coords[kTile , 1]
        if kTile != emptyTiles - 1:
            isValid[kTile + 1] = [True] * 9
            solution[coords[kTile + 1 , 0] , coords[kTile + 1 , 1]] = 0

        # store invalid answers in corresponding row (ascending order)
        for sCol in range(9):
            if solution[pRow , sCol] != 0:
                isValid[kTile , solution[pRow][sCol] - 1] = False
        for rRow in range(9):
            if solution[rRow , qCol] != 0:
                isValid[kTile , solution[rRow][qCol] - 1] = False
        quad = [math.floor(pRow/3) * 3,
                math.floor(qCol/3) * 3]
        for tRow in range(quad[0] , quad[0] + 3):
            for uCol in range(quad[1] , quad[1] + 3):
                if solution[tRow , uCol] != 0:
                    isValid[kTile , solution[tRow][uCol] - 1] = False
        
        # if there are no valid answers:
        if np.sum(isValid[kTile]) == 0:
            if kTile != 0:
                kTile -= 1
            elif kTile == 0:
                print("No solution exists.")
                return 0
        else:
            for vNum in range(9):
                if isValid[kTile , vNum]:
                    solution[pRow , qCol] = vNum + 1
                    isValid[kTile , vNum] = False
                    print(solution)
                    break
            kTile += 1
    return solution
            # index -= 1
            # if index = 0:
                # no solution
            # set tile to next valid answer and set corresponding boolean to 0
        # set empty tile to first valid answer and set corresponding boolean to 0
        # index += 1

# note: empty tiles contain 0

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
testBoard2 = np.array([
    [5,3,1,1,7,1,1,1,1],
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