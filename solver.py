import numpy as np

# solve function
    # verify dimensions
    # count n empty tiles
    # define n-by-9 boolean array in zeros
    # while index < n
        # find empty tile
        # store tile index (1 through n)
        # store valid answers in corresponding row (ascending order)
        # if there are no valid answers:
            # index -= 1
            # if index = 0:
                # no solution
            # set tile to next valid answer and set corresponding boolean to 0
        # set empty tile to first valid answer and set corresponding boolean to 0
        # index += 1

# note: empty tiles are those containing any other number than 1 through 9