from PriorityQueue import PriorityQueue
from SearchOperators import *


class PuzzleNode:

    def __init__(self, currentState, cost):

        self.state = currentState
        self.cost = cost
        self.actions = None
        self.children = None


    def getOperators(self):

        legalOperators = []
        # priorityQueue = PriorityQueue()
        for x in getListOperators():

            if x(0, self.state)[2] == 0:
                legalOperators.append(x)
                # priorityQueue.insert(x, x(0, self.state)[2])

        self.actions = legalOperators


        return legalOperators

    def getFutureNodes(self):

        futureNodes = []

        for x in self.actions:
            futureNodes.append(PuzzleNode(x(0, self.state)[0], self.cost + x(0, self.state)[1]))

        futureNodes.sort(key=lambda x: x.cost) #sort the futureNodes depending on their cost
        self.children = futureNodes


        return futureNodes

    def initializeOperatorsAndChildren(self):
        self.getOperators()
        self.getFutureNodes()

    def isGoalState(self, goalState, goalState2):

        # condition to completed puzzle
        # print(goalState1)
        if self.state == goalState or self.state == goalState2:
            print('You have reached the goal state!')
            return True
        else:
            print('Keep trying!')
            return False

