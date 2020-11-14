from General import *
from Heuristics import *
import sys
from UniformCostSearch import *
from PriorityQueue import *
import time

puzzleList = readFile("puzzleInput.txt")
sys.setrecursionlimit(10**6)
averageTimeStart = time.time()
for x in range(len(puzzleList)):

    openList = PriorityQueue()
    closedList = []
    # currentList = [[0, 6, 2, 1],
    #                [7, 5, 3, 4]]
    print(puzzleList[x])
    currentList = listTo2DList(puzzleList[x], 2)

    goalState1 = setGoalState1(currentList, 2)
    goalState2 = setGoalState2(len(list(chain.from_iterable(currentList))), 2)
    print('GOAL STATE 1:', goalState1)
    print('GOAL STATE 2:', goalState2)
    # goalState1 = [[1, 2, 3, 4],
    #                [5, 6, 7, 0]]
    #
    # goalState2 = goalState1

    currentNode = PuzzleNode(currentList, 0, 0)
    currentNode.initializeOperatorsAndChildren()
    openList.insert(currentNode, 0)
    startTime = time.time()
    uniformCostSearch(openList, closedList, goalState1, goalState2, startTime, x)

totalTimeEnd = time.time() - averageTimeStart
averageTimeEnd = totalTimeEnd/50
with open(r'analysis/analysisFile', 'w') as f:
    f.write('Total Time: ' + str(totalTimeEnd) + '\n')
    f.write('Average Time: ' + str(averageTimeEnd) + '\n')
    t.close()

writeToFileTotalCost()
writeToNoSolutionFile()

for x in range(len(puzzleList)):
    solutionFileName = generateFileName(x, 'UCS', 'Solution.txt')
    searchFileName = generateFileName(x, 'UCS', 'Search.txt')
    countFileLines(searchFileName, solutionFileName)

writeLineCountToCountFile()


# puzzle, goalState1, goalState2 = getPuzzle(puzzleList[0])
#
# print(puzzle)

# # iterate through list of puzzles and10
# === Starting State ===
# 1	2	3
# 4	5	0  do the necessary work!
# for x in range(len(puzzleList)):
#     print(listTo2DList(puzzleList[x], 2))
# goalstate1 = setGoalState1(puzzleList[x], 2)
# goalstate2 = setGoalState2(len(puzzleList[x]), 2)
#
#     puzzleList[x] = listTo2DList(puzzleList[x], 2)


# goalState = setGoalState1(puzzleList[0], 2)

# list = [3,0,1,4,2,6,5,7]


# checkGoalStates(goalState)
