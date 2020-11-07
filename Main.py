from General import *

puzzleList = readFile("testFile.txt")


puzzle, goalState1, goalState2 = getPuzzle(puzzleList[0])

print(puzzle)
print(goalState1)
print(goalState2)



# # iterate through list of puzzles and do the necessary work!
# for x in range(len(puzzleList)):
#     goalstate1 = setGoalState1(puzzleList[x], 2)
#     goalstate2 = setGoalState2(len(puzzleList[x]), 2)
#
#     puzzleList[x] = listTo2DList(puzzleList[x], 2)


# goalState = setGoalState1(puzzleList[0], 2)

# list = [3,0,1,4,2,6,5,7]


# checkGoalStates(goalState)