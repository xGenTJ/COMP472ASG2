from itertools import chain

import numpy as np
from Heuristics import *


goalState1 = [[1, 2, 3, 4],
              [5, 6, 7, 0]]

goalState2 = [[1, 3, 5, 7],
              [2, 4, 6, 0]]

someRandomState = [[1, 3, 5, 7],
              [2, 4, 6, 0]]


# To flatten 2d lists when writing to final files
def flattenOutList(list):
    flatList = []
    for x in list:
        flatList.extend(x)
    print(flatList)
# example
# flattenOutState(goalState1)


def readFile(fileName):
    f = open(fileName, "r")
    puzzleList = []
    for line in f:

      line = line.strip('\n')

      newList = list(line.split(" "))
      newList = list(map(int, newList))

      # print(newList)
      puzzleList.append(newList)

    # print(puzzleList)

    return puzzleList


def listTo2DList(list, nbrows):
    listSize = len(list)

    newList = []

    tempList = list[0:int(listSize/nbrows)]
    tempList2 = list[int(listSize/nbrows):listSize]
    newList.append(tempList)
    newList.append(tempList2)

    return newList

def setGoalState1(twoDlist, nbrows):

    newList = list(chain.from_iterable(twoDlist))

    listSize = len(newList)
    newList = sorted(newList)
    newList.append(newList.pop(0))
    goalState = []

    tempList = newList[0:int(listSize/nbrows)]
    tempList2 = newList[int(listSize/nbrows):listSize]
    goalState.append(tempList)
    goalState.append(tempList2)
    return goalState

def setGoalState2(nbelements, nbrows):

    goalState = []
    index = 1
    tempArray = []

    for row in range(nbrows):

        for x in range(index, nbelements, nbrows):
            # print(x)
            tempArray.append(x)

        # print(tempArray)
        goalState.append(tempArray[:])
        index += 1
        tempArray.clear()

    goalState[-1].append(0)

    # print(goalState)

    return goalState


def getPuzzle(list):

    goalstate1 = setGoalState1(list, 2)
    goalstate2 = setGoalState2(len(list), 2)
    puzzle = listTo2DList(list, 2)

    return puzzle, goalState1, goalState2


state = [[0, 2, 3, 4],
         [5, 6, 7, 1]]

goalState = [[6, 5, 7, 3],
             [2, 0, 4, 1]]

# print(hammingDistance(state, goalState))
# print(manhattanDistance(state, goalState))