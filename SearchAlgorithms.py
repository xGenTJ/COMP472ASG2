import os
import sys
from pandas import *
from Heuristics import get2dIndex
import copy

totalCost = 0

def moveLeft(number, currentState):
    futureState = copy.deepcopy(currentState)

    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX - 1
    futureY = currentY
    try:
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' to the left for a cost of 1')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')
        global totalCost
        totalCost +=1
    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        print(exc_type, fname, exc_tb.tb_lineno)

        return None

    return futureState


def moveRight(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX + 1
    futureY = currentY

    try:
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' to the right for a cost of 1')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')
        global totalCost
        totalCost +=1
    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        print(exc_type, fname, exc_tb.tb_lineno)

        return None

    return futureState


def moveUp(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX
    futureY = currentY - 1

    try:
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' up for a cost of 1')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')
        global totalCost
        totalCost +=1
    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        print(exc_type, fname, exc_tb.tb_lineno)

        return None

    return futureState


def moveDown(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX
    futureY = currentY + 1

    try:
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' down for a cost of 1')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')
        global totalCost
        totalCost +=1
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)
        return None

    return futureState


def moveDiagonalUpLeft(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX - 1
    futureY = currentY - 1
    # print("current position: (", currentX, ", ", currentY, ")")
    # print("future position: (", futureX, ", ", futureY, ")")
    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up left")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' diagonally up left for a cost of 3')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')
        global totalCost
        totalCost += 3
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)
        return None

    return futureState


def moveDiagonalUpRight(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX + 1
    futureY = currentY - 1

    # print("current position: (", currentX, ", ", currentY, ")")
    # print("future position: (", futureX, ", ", futureY, ")")

    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up right")
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' diagonally up right for a cost of 3')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')
        global totalCost
        totalCost += 3
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)
        return None

    return futureState


def moveDiagonalDownLeft(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX - 1
    futureY = currentY + 1

    # print("current position: (", currentX, ", ", currentY, ")")
    # print("future position: (", futureX, ", ", futureY, ")")

    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving down left")
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' diagonally down left for a cost of 3')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')
        global totalCost
        totalCost += 3
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)
        return None

    return futureState


def moveDiagonalDownRight(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX + 1
    futureY = currentY + 1
    # print("current position: (", currentX, ", ", currentY, ")")
    # print("future position: (", futureX, ", ", futureY, ")")
    global totalCost
    totalCost += 3
    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving down right")
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        print('Moved ', number, ' diagonally down right for a cost of 3')
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)
        return None

    return futureState


currentList = [[1, 2, 3],
               [4, 5, 0]]

print('=== Starting State ===')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentList]), '\n')

try:
    future = moveLeft(0, currentList)
    future = moveRight(1, future)
    future = moveUp(5, future)
    future = moveDown(1, future)
    future = moveDiagonalDownRight(0, future)
    future = moveDiagonalUpRight(4, future)
    future = moveDiagonalUpLeft(1, future)
    future = moveDiagonalDownLeft(5, future)
    print('Total Cost: ', totalCost)
except TypeError:
    print('Encountered Error')
