import numpy as np


def get2dIndex(myList, v):
    for x, y in enumerate(myList):
        if v in y:
            return x, y.index(v)


def h0(state, goalState):

    return get2dIndex(state, 0) == get2dIndex(goalState, 0)


def hammingDistance(state, goalState):
    return (np.array(state) == np.array(goalState)).sum() - 1


def manhattanDistance(state, goalState):
    manDist = 0
    currentRow = 0
    currentColumn = 0
    goalRow = 0
    goalColumn = 0
    rowDistance = 0
    columnDistance = 0

    for row in range(len(state)):  # iterating thru all the rows

        for element in state[row]:  # iterating thru all the columns

            if element != 0:
                currentRow, currentColumn = get2dIndex(state, element)
                goalRow, goalColumn = get2dIndex(goalState, element)

                rowDistance += abs(currentRow - goalRow)
                columnDistance += abs(currentColumn - goalColumn)

    manDist = rowDistance + columnDistance

    return manDist

    # def calculate(value, goalList):
    #
    #     row = 0
    #     column = 0
    #
    #     for list in goalList:
    #
    #         for element in list:

