import time
from graphviz import Graph
from PriorityQueue import *
from PuzzleNode import *
from General import *
import sys


def uniformCostSearch(openList, closedList, goalState1, goalState2, startTime, searchIndex):
    # currentNode should be the first node of the sorted openList (priority queue)
    currentExecutionTime = time.time() - startTime
    print('TIME ELAPSED:', currentExecutionTime)
    currentNode = openList.remove()
    isGoalState = currentNode.isGoalState(goalState1, goalState2)
    solutionFileName = generateFileName(searchIndex, 'UCS', 'Solution.txt')
    searchFileName = generateFileName(searchIndex, 'UCS', 'Search.txt')

    if currentExecutionTime > 60:
        print('Reached max timer')
        overWriteFiles(searchFileName, solutionFileName)
        return

    if isGoalState:
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')
        print('Cost of going to goal state:', currentNode.cost)
        print('SOLUTION PATH:')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')
        finalCost = currentNode.totalCost
        # finalSolution = ('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.parent.state]))
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
                openList.insert(x, x.totalCost)
                print('Node Option ' + str(i) + ' inserted into openList\n')
                i += 1

            else:
                print('child already in closed list')


    print("OPEN LIST:\n\n", openList.toString())
    print("CLOSED LIST:\n")

    for x in closedList:
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x]), '\n')

    uniformCostSearch(openList, closedList, goalState1, goalState2, startTime, searchIndex)


    return None







