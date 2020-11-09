import time
from graphviz import Graph
from PriorityQueue import *
from PuzzleNode import *


def uniformCostSearch(currentNode, goalState1, goalState2):

    print("CURRENT NODE: ", currentNode.state)

    if currentNode.isGoalState(goalState1, goalState2) == False:

        print('current State:', currentNode.state, ' | cost: ', currentNode.cost)

        currentNode.initializeOperatorsAndChildren()

        for x in (currentNode.children):

            uniformCostSearch(x, goalState1, goalState2)

    print("END OF RECURSION, FINAL STATE:", currentNode.state)
    return






