from General import *
from Heuristics import *
import sys
from UniformCostSearch import *
from GreedyBestFirstSearch import *
from PriorityQueue import *
from AStar import *
import time

puzzleList = readFile("puzzleInput.txt")
sys.setrecursionlimit(10 ** 6)
averageTimeStart = time.time()
numberOfPuzzles = len(puzzleList)
# numberOfPuzzles = 1
currentList = [[3, 7, 10, 1, 5, 8],
               [11, 0, 6, 9, 2, 4]]

openList = PriorityQueue()
closedList = []
# currentList = listTo2DList(currentList, 3)
goalState1 = setGoalState1(currentList, 2)
goalState2 = setGoalState2(len(list(chain.from_iterable(currentList))), 2)
print('GOAL STATE 1:', goalState1)
print('GOAL STATE 2:', goalState2)

currentNode = PuzzleNode(currentList, 0, 0)
currentNode.initializeOperatorsAndChildren()
openList.insert(currentNode, 0)
startTime = time.time()
AStar(openList, closedList, goalState1, goalState2, startTime, 0)

totalTimeEnd = time.time() - averageTimeStart
averageTimeEnd = totalTimeEnd / numberOfPuzzles

with open(r'analysis/Scaled/timeFile', 'w') as f:
    f.write('Total Time: ' + str(totalTimeEnd) + '\n')
    f.write('Average Time: ' + str(averageTimeEnd) + '\n')
    f.close()

solutionFileName = generateFileName(0, 'Scaled', 'Solution.txt')
searchFileName = generateFileName(0, 'Scaled', 'Search.txt')
countFileLines(searchFileName, solutionFileName)
countCosts(solutionFileName)

writeLineCountToCountFile(3, numberOfPuzzles)
writeToNoSolutionFile(3)
writeToFileTotalCost(3, numberOfPuzzles)
