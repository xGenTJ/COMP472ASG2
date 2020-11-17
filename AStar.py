import time
from graphviz import Graph
from PriorityQueue import *
from PuzzleNode import *
from General import *
import sys


def AStar(openList, closedList, goalState1, goalState2, startTime, searchIndex):
    currentExecutionTime = time.time() - startTime

    print('TIME ELAPSED:', currentExecutionTime)
    currentNode = openList.remove()
    isGoalState = currentNode.isGoalState(goalState1, goalState2)
    solutionFileName = generateFileName(searchIndex, 'Astar', 'Solution.txt')
    searchFileName = generateFileName(searchIndex, 'Astar', 'Search.txt')
    # solutionFileName = generateFileName(searchIndex, 'Scaled', 'Solution.txt')
    # searchFileName = generateFileName(searchIndex, 'Scaled', 'Search.txt')

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
        closedList.append(currentNode)

        appendToSearchFile(searchFileName, 0, currentNode.totalCost, 0, currentNode.state)
        print('currentNode placed in the closedList')
        print('current State:')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')
        print('current cost:', currentNode.cost)
        currentNode.initializeOperatorsAndChildren()
        print(currentNode.getOperators())
        i = 1

        for x in currentNode.children:

            if any(x.state == y.state and x.totalCost < y.totalCost for y in
                   closedList):  # if there are matching states in closedlist where x has a smaller cost
                closedList = [y for y in closedList if
                              y.state != x.state]  # keep only the entries in closedlist that don't match states with current x

            if not any(y.state == x.state for y in closedList):  # if no nodes in closedList have matching state with x

                print('Node Option ' + str(i))
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x.state]), '\n')
                x.parent = currentNode
                # openList.insert(x, x.totalCost + hammingDistance(x.state, goalState1, goalState2))  # g(n) + h(n)
                openList.insert(x, x.totalCost + manhattanDistance(x.state, goalState1, goalState2))  # g(n) + h(n)
                # openList.insert(x, x.totalCost + h0(x.state, goalState1))  # g(n) + h(n)
                print('Node Option ' + str(i) + ' inserted into openList\n')
                i += 1

            else:
                print('child already in closed list')

    print("OPEN LIST:\n\n", openList.toString())
    print("CLOSED LIST:\n")

    for x in closedList:
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x.state]), '\n')

    AStar(openList, closedList, goalState1, goalState2, startTime, searchIndex)

    return None
