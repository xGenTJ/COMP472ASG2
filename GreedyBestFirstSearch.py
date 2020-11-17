import time
from graphviz import Graph
from PriorityQueue import *
from PuzzleNode import *
from General import *
import sys


def greedyBestFirstSearch(openList, closedList, goalState1, goalState2, startTime, searchIndex):

    currentExecutionTime = time.time() - startTime

    print('TIME ELAPSED:', currentExecutionTime)
    currentNode = openList.remove()
    isGoalState = currentNode.isGoalState(goalState1, goalState2)
    solutionFileName = generateFileName(searchIndex, 'GBFS', 'Solution.txt')
    searchFileName = generateFileName(searchIndex, 'GBFS', 'Search.txt')

    if currentExecutionTime > 60:
        print('Reached max timer')
        addToNoSolution()
        overWriteFiles(searchFileName, solutionFileName)
        return

    if isGoalState:
        print('Cost of going to goal state:', currentNode.cost)
        print('SOLUTION PATH:')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')
        finalCost = currentNode.totalCost
        while currentNode.parent is not None:
            currentY, currentX = get2dIndex(currentNode.state, 0)
            swappedNumber = currentNode.parent.state[currentY][currentX]
            print('SWAPPED NUMBER: ', swappedNumber)
            appendToSolutionFile(solutionFileName, swappedNumber, currentNode.cost, currentNode.state)
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.parent.state]), '\n')
            currentNode = currentNode.parent

        appendToSolutionFile(currentNode, 0, currentNode.cost, currentNode.state)
        writeFinalSearchPath(searchFileName)
        WriteFinalSolutionFile(solutionFileName, finalCost, currentExecutionTime)
        print('FINAL COST:', finalCost)
        addToTotalCost(finalCost)
        return True

    else:
        closedList.append(currentNode.state)

        appendToSearchFile(searchFileName, 0, currentNode.totalCost, 0, currentNode.state)
        print('currentNode placed in the closedList')
        print('current State:')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')
        print('current cost:', currentNode.cost)
        currentNode.initializeOperatorsAndChildren()
        print(currentNode.getOperators())
        i = 1

        for x in currentNode.children:

            if x.state not in closedList:

                print('Node Option ' + str(i))
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x.state]), '\n')
                x.parent = currentNode
                openList.insert(x, hammingDistance(x.state, goalState1, goalState2))
                # openList.insert(x, manhattanDistance(x.state, goalState1, goalState2))
                # openList.insert(x, h0(x.state, goalState1))
                print('Node Option ' + str(i) + ' inserted into openList\n')
                i += 1

            else:
                print('child already in closed list')


    print("OPEN LIST:\n\n", openList.toString())
    print("CLOSED LIST:\n")

    for x in closedList:
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x]), '\n')

    greedyBestFirstSearch(openList, closedList, goalState1, goalState2, startTime, searchIndex)


    return None







