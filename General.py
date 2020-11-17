from itertools import chain
import sys
import random
import numpy as np
from Heuristics import *
solutionFileLines = []
searchFileLines = []
totalCost = 0
totalNoSolution = 0
searchCount = 0
solutionCount = 0
averageCost = 0

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
    return flatList
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


def listTo2DList(passedList, nbrows):
    listSize = len(passedList)

    newList = []

    tempList = passedList[0:int(listSize/nbrows)]
    tempList2 = passedList[int(listSize/nbrows):listSize]
    newList.append(tempList)
    newList.append(tempList2)

    return newList

def generatePuzzles():
    number_list = [0, 1, 2, 3, 4, 5, 6, 7]
    for x in range(50):
        # print("Original list:", number_list)
        #
        # random.shuffle(number_list)
        # print("List after shuffle:", number_list)

        listToStr = ' '.join([str(elem) for elem in number_list])

        # print(listToStr)

        if x != 49:
            listToStr = listToStr + '\n'
        else:
            listToStr = listToStr

        with open(r'puzzleInput.txt', 'a') as f:
            f.write(listToStr)

def setGoalState1(twoDlist, nbrows):

    newList = list(chain.from_iterable(twoDlist))
    listSize = len(newList)
    elementPerRow = int(listSize/nbrows)
    newList = sorted(newList)
    newList.append(newList.pop(0))
    goalState = []
    i = 0
    j = 1
    for x in range(nbrows):
        goalState.append(newList[i: elementPerRow * j])
        i += elementPerRow
        j += 1
    # tempList = newList[0:int(listSize/nbrows)]
    # tempList2 = newList[int(listSize/nbrows):listSize]
    # goalState.append(tempList)
    # goalState.append(tempList2)
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

def generateFileName(puzzleIndex, searchAlgoName, fileType):

    fileName = searchAlgoName + '/' + str(puzzleIndex) + "_" + searchAlgoName + "_" + fileType
    return fileName

def appendToSearchFile(fileName, fn, gn, hn, state):
    # to be called for each node traverse -> contains the search path
    # if fn, gn, or hn are irrelevant, display 0
    global searchFileLines
    newState = flattenOutList(state)
    listToStr = ' '.join([str(elem) for elem in newState])
    searchFileLines.append((str(fn) + " " + str(gn) + " " + str(hn) + " " + listToStr + "\n"))
    # with open(r'searchFiles/' + fileName, 'a') as f:
    #     # f.write(str(fn) + " " + str(gn) + " " + str(hn) + " " + listToStr + "\n")
    #     f.write(searchFileLines[-1])


def writeFinalSearchPath(fileName):
    with open(r'searchFiles/' + fileName, 'a') as f:

        for x in range(0, len(searchFileLines)):
            f.write(searchFileLines[len(searchFileLines)-x -1])

    f.close()
    searchFileLines.clear()

def appendToSolutionFile(fileName, tileMoved, cost, state):
    # to be called if final NOT final solution
    # tileMoved is the value of the tile that we switched with zero
    # cost is the cost of the individual move (NOT overall cost)
    # state is always the updated state
    global solutionFileLines
    newState = flattenOutList(state)
    listToStr = ' '.join([str(elem) for elem in newState])
    solutionFileLines.append((str(tileMoved) + " " + str(cost) + " " + listToStr + "\n"))
    # with open(r'solutionFiles/' + fileName, 'a') as f:
    #     f.write(str(tileMoved) + " " + str(cost) + " " + listToStr + "\n")


def WriteFinalSolutionFile(fileName, cost, executionTime):
    # to be called when final solution is found --> SOLUTION EXISTS
    # cost is the cost of total solution path cost
    # appends the solution to the file
    global solutionFileLines
    with open(r'solutionFiles/' + fileName, 'a') as f:

        for x in range(0, len(solutionFileLines)):
            f.write(solutionFileLines[len(solutionFileLines)-x -1])

        f.write('\n' + str(cost) + " " + str(executionTime) + "\n\n")

    f.close()
    solutionFileLines.clear()


def overWriteFiles(searchFileName, solutionFileName):
    # to be called if we time out before finding a solution
    # will overwrite to search file
    with open(r'searchFiles/' + searchFileName, 'w') as f:
        f.write("no solution")
        f.close()
    with open(r'solutionFiles/' + solutionFileName, 'w') as f:
        f.write("no solution")
        f.close()

def addToTotalCost(cost):
    global totalCost
    totalCost += cost
    return totalCost

def writeToFileTotalCost(algo, numberOfPuzzles):
    global totalCost

    if algo == 0:
        with open(r'analysis/UCS/totalCost', 'w') as f:
            f.write('Total Cost: ' + str(totalCost) + '\n')
            f.write('Average Cost: ' + str(totalCost/(numberOfPuzzles-(totalNoSolution/2))) + '\n')
            f.close()

    elif algo == 1:
        with open(r'analysis/GBFS/totalCost', 'w') as f:
            f.write('Total Cost: ' + str(totalCost) + '\n')
            f.write('Average Cost: ' + str(totalCost/(numberOfPuzzles-(totalNoSolution/2))) + '\n')
            f.close()

    elif algo == 2:
        with open(r'analysis/Astar/totalCost', 'w') as f:
            f.write('Total Cost: ' + str(totalCost) + '\n')
            f.write('Average Cost: ' + str(totalCost/(numberOfPuzzles-(totalNoSolution/2))) + '\n')
            f.close()
    elif algo == 3:
        with open(r'analysis/Scaled/totalCost', 'w') as f:
            f.write('Total Cost: ' + str(totalCost) + '\n')
            f.write('Average Cost: ' + str(totalCost/(numberOfPuzzles-(totalNoSolution/2))) + '\n')
            f.close()

def countCosts(solutionFileName):

    global totalCost
    global averageCost

    with open(r'solutionFiles/' + solutionFileName, 'r') as f:
        for line in f:
            listLine = list(line.split(' '))
            if 'no solution' not in line:

                if len(listLine) == 2:
                    totalCost += float(listLine[0])

        f.close()

def countFileLines(searchFileName, solutionFileName):
    global searchCount, solutionCount
    with open(r'searchFiles/' + searchFileName, 'r') as f:
        for line in f:
            if 'no solution' in line:
                addToNoSolution()
                continue
            else:
                searchCount += 1
        f.close()
    with open(r'solutionFiles/' + solutionFileName, 'r') as f:
        for line in f:
            if 'no solution' in line:
                addToNoSolution()
                continue
            else:
                solutionCount += 1
        f.close()

    return searchCount, solutionCount

def writeLineCountToCountFile(algo, numberOfPuzzles):
    global searchCount, solutionCount, totalNoSolution

    if algo == 0:
        with open(r'analysis/UCS/countFile', 'w') as f:
            f.write('Total Search Steps: ' + str(searchCount) + '\n')
            f.write('Average Search Steps: ' + str(searchCount/(numberOfPuzzles-(totalNoSolution/2))) + '\n')
            f.write('Total Solution Steps: ' + str(solutionCount) + '\n')
            f.write('Average Solution Steps: ' + str(solutionCount/(numberOfPuzzles-(totalNoSolution/2))) + '\n')
            f.close()
    if algo == 1:
        with open(r'analysis/GBFS/countFile', 'w') as f:
            f.write('Total Search Steps: ' + str(searchCount) + '\n')
            f.write('Average Search Steps: ' + str(searchCount/(50-(totalNoSolution/2))) + '\n')
            f.write('Total Solution Steps: ' + str(solutionCount) + '\n')
            f.write('Average Solution Steps: ' + str(solutionCount/(numberOfPuzzles-(totalNoSolution/2))) + '\n')
            f.close()
    if algo == 2:
        with open(r'analysis/Astar/countFile', 'w') as f:
            f.write('Total Search Steps: ' + str(searchCount) + '\n')
            f.write('Average Search Steps: ' + str(searchCount / (numberOfPuzzles - (totalNoSolution / 2))) + '\n')
            f.write('Total Solution Steps: ' + str(solutionCount) + '\n')
            f.write(
                'Average Solution Steps: ' + str(solutionCount / (numberOfPuzzles - (totalNoSolution / 2))) + '\n')
            f.close()
    if algo == 3:
        with open(r'analysis/Scaled/countFile', 'w') as f:
            f.write('Total Search Steps: ' + str(searchCount) + '\n')
            f.write('Average Search Steps: ' + str(searchCount / (numberOfPuzzles - (totalNoSolution / 2))) + '\n')
            f.write('Total Solution Steps: ' + str(solutionCount) + '\n')
            f.write('Average Solution Steps: ' + str(solutionCount / (numberOfPuzzles - (totalNoSolution / 2))) + '\n')
            f.close()

def addToNoSolution():
    global totalNoSolution
    totalNoSolution += 1

def writeToNoSolutionFile(algo):
    global totalNoSolution

    if algo == 0:
        with open(r'analysis/UCS/noSolution', 'w') as f:
            f.write('Total files with no solution: ' + str(totalNoSolution/2) + '\n')
            f.close()
    if algo == 1:
        with open(r'analysis/GBFS/noSolution', 'w') as f:
            f.write('Total files with no solution: ' + str(totalNoSolution/2) + '\n')
            f.close()
    if algo == 2:
        with open(r'analysis/Astar/noSolution', 'w') as f:
            f.write('Total files with no solution: ' + str(totalNoSolution/2) + '\n')
            f.close()
    if algo == 3:
        with open(r'analysis/Scaled/noSolution', 'w') as f:
            f.write('Total files with no solution: ' + str(totalNoSolution/2) + '\n')
            f.close()

