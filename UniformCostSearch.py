import time
from graphviz import Graph
from PriorityQueue import *
from PuzzleNode import *


def uniformCostSearch(openList, closedList, goalState1, goalState2):
    # currentNode should be the first node of the sorted openList (priority queue)
    currentNode = openList.remove()
    if currentNode.isGoalState(goalState1, goalState2) == True:
        print('goal state found! now process this shit yo!')
        return
    if currentNode.isGoalState(goalState1, goalState2) == False:
        closedList.insert(currentNode, 0)
        print('currentNode placed in the closedList')
        print('current State:')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentNode.state]), '\n')

        currentNode.initializeOperatorsAndChildren()

        i = 1
        for x in (currentNode.children):
            print('Node Option ' + str(i))
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in x.state]), '\n')
            if x.isGoalState(goalState1, goalState2):
                print('goal state found! now process this shit yo!')
                return
            else:
                openList.insert(x, 0)
                print('Node Option ' + str(i) + ' inserted into openList\n')
            # print(x.isGoalState(goalState1, goalState2))
            i += 1

        # SORT OPENLIST HERE
        # uniformCostSearch(openList, closedList, goalState1, goalState2)
    print("END OF RECURSION, FINAL STATE:", currentNode.state)
    return None






