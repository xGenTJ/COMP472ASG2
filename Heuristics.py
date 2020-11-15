import numpy as np


def get2dIndex(myList, v):
    for x, y in enumerate(myList):
        if v in y:
            return x, y.index(v)


def h0(state, goalState):
    if get2dIndex(state, 0) == get2dIndex(goalState, 0):
        return 0
    else:
        return 1


def hammingDistance(state, goalState1, goalState2):

    differenceState1 = 0
    differenceState2 = 0

    for sublist in state:
        for element in sublist:
            if element != 0:
                if get2dIndex(state, element) != get2dIndex(goalState1, element):
                    differenceState1 += 1

    for sublist in state:
        for element in sublist:
            if element != 0:
                if get2dIndex(state, element) != get2dIndex(goalState2, element):
                    differenceState2 += 1

    return min(differenceState1, differenceState2)


def manhattanDistance(state, goalState1, goalState2):
    manDist1 = 0
    manDist2 = 0
    currentRow = 0
    currentColumn = 0
    goalRow = 0
    goalColumn = 0
    rowDistance1 = 0
    columnDistance1 = 0
    rowDistance2 = 0
    columnDistance2 = 0

    for row in range(len(state)):  # iterating thru all the rows

        for element in state[row]:  # iterating thru all the columns

            if element != 0:
                currentRow, currentColumn = get2dIndex(state, element)
                goalRow, goalColumn = get2dIndex(goalState1, element)

                rowDistance1 += abs(currentRow - goalRow)
                columnDistance1 += abs(currentColumn - goalColumn)

    manDist1 = rowDistance1 + columnDistance1

    for row in range(len(state)):  # iterating thru all the rows

        for element in state[row]:  # iterating thru all the columns

            if element != 0:
                currentRow, currentColumn = get2dIndex(state, element)
                goalRow, goalColumn = get2dIndex(goalState2, element)

                rowDistance2 += abs(currentRow - goalRow)
                columnDistance2 += abs(currentColumn - goalColumn)

    manDist2 = rowDistance2 + columnDistance2

    return min(manDist1, manDist2)

# currentList = [[1, 6, 2, 0],
#                 [3, 5, 7, 4]]
#
# goalState1 = [[1, 2, 3, 4],
#                 [5, 6, 7, 0]]
# print(hammingDistance(currentList, goalState1))
