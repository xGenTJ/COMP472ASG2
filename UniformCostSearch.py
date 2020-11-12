import time
from graphviz import Graph
from PriorityQueue import *
from PuzzleNode import *
from General import *
import sys

def uniformCostSearch(openList, closedList, goalState1, goalState2, maxRecursion):
    # currentNode should be the first node of the sorted openList (priority queue)
    currentNode = openList.remove()
    isGoalState = currentNode.isGoalState(goalState1, goalState2)
    solutionFileName = generateFileName(1, 'UCS', 'Solution.txt')
    searchFileName = generateFileName(1, 'UCS', 'Search.txt')

    if isGoalState:
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')
        print('Cost of going to goal state:', currentNode.cost)
        print('SOLUTION PATH:')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')
        finalCost = currentNode.cost
        finalSolution = ('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.parent.state]))
        while currentNode.parent is not None:

            finalCost += currentNode.parent.cost

            appendToSolutionFile(solutionFileName, 0, currentNode.parent.cost, currentNode.state)
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.parent.state]), '\n')
            currentNode = currentNode.parent

        writeFinalSearchPath(searchFileName)
        appendFinalSolutionToSolutionFile(solutionFileName, finalCost, 0)
        print('FINAL COST:', finalCost)
        return True

    elif maxRecursion == 0:
        print('Reached max recursion')
        sys.exit()

    else:
        closedList.append(currentNode.state)
        appendToSearchFile(searchFileName, 0, currentNode.getTotalCost(), 0, currentNode.state)
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
                openList.insert(x, x.cost)
                print('Node Option ' + str(i) + ' inserted into openList\n')
                i += 1

            else:
                print('child already in closed list')


    print("OPEN LIST:\n\n", openList.toString())
    print("CLOSED LIST:\n")

    for x in closedList:
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x]), '\n')

    uniformCostSearch(openList, closedList, goalState1, goalState2, maxRecursion-1)


    return None







