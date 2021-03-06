from General import *
from Heuristics import *
import sys
from UniformCostSearch import *
from GreedyBestFirstSearch import *
from PriorityQueue import *
import time

puzzleList = readFile("puzzleInput.txt")
sys.setrecursionlimit(10**6)
averageTimeStart = time.time()
numberOfPuzzles = len(puzzleList)

for x in range(len(puzzleList)):
    openList = PriorityQueue()
    closedList = []
    currentList = listTo2DList(puzzleList[x], 2)
    goalState1 = setGoalState1(currentList, 2)
    goalState2 = setGoalState2(len(list(chain.from_iterable(currentList))), 2)
    print('GOAL STATE 1:', goalState1)
    print('GOAL STATE 2:', goalState2)

    currentNode = PuzzleNode(currentList, 0, 0)
    currentNode.initializeOperatorsAndChildren()
    openList.insert(currentNode, 0)
    startTime = time.time()
    greedyBestFirstSearch(openList, closedList, goalState1, goalState2, startTime, x)

totalTimeEnd = time.time() - averageTimeStart
averageTimeEnd = totalTimeEnd/50

with open(r'analysis/GBFS/timeFile', 'w') as f:
    f.write('Total Time: ' + str(totalTimeEnd) + '\n')
    f.write('Average Time: ' + str(averageTimeEnd) + '\n')
    f.close()

for x in range(len(puzzleList)):
    solutionFileName = generateFileName(x, 'GBFS', 'Solution.txt')
    searchFileName = generateFileName(x, 'GBFS', 'Search.txt')
    countFileLines(searchFileName, solutionFileName)
    countCosts(solutionFileName)

writeLineCountToCountFile(1, numberOfPuzzles)
writeToNoSolutionFile(1)
writeToFileTotalCost(1, numberOfPuzzles)

