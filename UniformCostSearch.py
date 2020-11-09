import time
from graphviz import Graph
from PriorityQueue import *
from PuzzleNode import *


def uniformCostSearch(currentNode, goalState1, goalState2):

    if currentNode.isGoalState(goalState1, goalState2) == False:

        print('current State:')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')

        currentNode.initializeOperatorsAndChildren()

        for x in (currentNode.children):

            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x.state]), '\n')
            print(x.isGoalState(goalState1, goalState2))
            # uniformCostSearch(x, goalState1, goalState2)

    print("END OF RECURSION, FINAL STATE:", currentNode.state)
    return None






