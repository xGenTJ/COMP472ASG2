from General import *
from Heuristics import *
from UniformCostSearch import  *
# puzzleList = readFile("testFile.txt")

currentList = [[1, 2, 3, 4],
               [5, 6, 7, 0]]

currentNode = PuzzleNode(currentList, 0)
currentNode.initializeOperatorsAndChildren()
# goalstate1 = [[1,2,3,4],[5,6,7,0]]
goalstate1 = setGoalState1(currentList, 2)
goalstate2 = setGoalState2(len(list(chain.from_iterable(currentList))), 2)

uniformCostSearch(currentNode, goalstate1, goalstate2)

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