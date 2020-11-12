import os
import sys
from pandas import *
from Heuristics import get2dIndex
import copy


# totalCost = 0

def moveLeft(number, currentState):
    futureState = copy.deepcopy(currentState)

    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX - 1
    futureY = currentY
    errorCode = 0
    cost = 1

    try:

        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up left")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'to the left for a cost of 1')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')



    except Exception as e:

        errorCode = 1

        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        # print(exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def moveRight(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX + 1
    futureY = currentY
    errorCode = 0
    cost = 1

    try:

        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up left")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'to the right for a cost of 1')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')


    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        # print(exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def moveUp(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX
    futureY = currentY - 1
    errorCode = 0
    cost = 1
    # print('Current X and Y:', currentX, currentY)
    # print('Future X and Y:', futureX, futureY)
    try:

        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up left")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'up for a cost of 1')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')

    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        # print(exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def moveDown(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX
    futureY = currentY + 1
    errorCode = 0
    cost = 1

    try:

        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up left")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'down for a cost of 1')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')


    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #  print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def moveDiagonalUpLeft(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX - 1
    futureY = currentY - 1
    errorCode = 0
    cost = 3

    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up left")

        elif not ((currentX == 0 or currentX == len(currentState[0]) - 1) and (
                currentY == 0 or currentY == len(currentState[0]) - 1)):
            raise IndexError("Index Error moving up left")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'diagonally up left for a cost of 3')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')


    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #  print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def moveDiagonalUpRight(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX + 1
    futureY = currentY - 1
    errorCode = 0
    cost = 3

    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving up right")

        elif not ((currentX == 0 or currentX == len(currentState[0]) - 1) and (
                currentY == 0 or currentY == len(currentState[0]) - 1)):
            raise IndexError("Index Error moving up right")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'diagonally up right for a cost of 3')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')


    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #  print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def moveDiagonalDownLeft(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX - 1
    futureY = currentY + 1
    errorCode = 0
    cost = 3

    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving down left")

        elif not ((currentX == 0 or currentX == len(currentState[0]) - 1) and (
                currentY == 0 or currentY == len(currentState[0]) - 1)):
            raise IndexError("Index Error moving down left")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'diagonally down left for a cost of 3')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')


    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #  print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def moveDiagonalDownRight(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureX = currentX + 1
    futureY = currentY + 1
    errorCode = 0
    cost = 3

    try:
        if futureX < 0 or futureY < 0:
            raise IndexError("Index Error moving down right")

        elif not ((currentX == 0 or currentX == len(currentState[0]) - 1) and (

                currentY == 0 or currentY == len(currentState[0]) - 1)):
            raise IndexError("Index Error moving down right")

        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Moved', number, 'diagonally down right for a cost of 3')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')

    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #  print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def specialDiagonal(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)

    errorCode = 0
    cost = 3
    try:
        if currentX == 0:
            if currentY == 0:  # top left corner
                futureX = -1
                futureY = -1  # moves to bottom right

            else:  # bottom left corner
                futureX = -1
                futureY = 0  # moves to top right

        elif currentX == len(currentState[0]) - 1:

            if currentY == 0:  # top right corner
                futureX = 0
                futureY = -1  # moves to bottom left

            else:  # bottom right corner
                futureX = 0
                futureY = 0  # moves to top left

        else:
            raise IndexError("Index Error moving diagonally specially")

            swappedNumber = currentState[futureY][futureX]

            futureState[futureY][futureX] = number
            futureState[currentY][currentX] = swappedNumber
            # print('Moved', number, 'special diagonally for a cost of 3')
            # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')

    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def wrapAround(number, currentState):
    futureState = copy.deepcopy(currentState)
    currentY, currentX = get2dIndex(currentState, number)
    futureY = currentY
    errorCode = 0
    cost = 2

    if currentX == 0:  # if at the beginning of the row
        futureX = -1

    elif currentX == len(currentState[0]) - 1:  # if at the end of the row
        futureX = 0

    try:
        swappedNumber = currentState[futureY][futureX]

        futureState[futureY][futureX] = number
        futureState[currentY][currentX] = swappedNumber
        # print('Wrapped', number, 'around for a cost of 2')
        # # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in futureState]), '\n')

    except Exception as e:
        errorCode = 1
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # print('Invalid Move: ', exc_type, fname, exc_tb.tb_lineno)

    return [futureState, cost, errorCode]


def getListOperators():
    return [moveUp, moveDown, moveLeft, moveRight, moveDiagonalUpLeft, moveDiagonalUpRight, moveDiagonalDownLeft,
            moveDiagonalDownRight, specialDiagonal, wrapAround]

# currentList = [[1, 2, 3],
#                [4, 5, 0]]
#
# print('=== Starting State ===')
# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in currentList]), '\n')

# try:
#
#     future = moveLeft(0, currentList)[0]
#     future = moveRight(1, future)[0]
#     future = moveUp(5, future)[0]
#     future = moveDown(1, future)[0]
#     future = moveDiagonalDownRight(0, future)[0]
#     future = moveDiagonalUpRight(4, future)[0]
#     future = moveDiagonalUpLeft(1, future)[0]
#     future = moveDiagonalDownLeft(5, future)[0]
#     future = wrapAround(3, future)[0]
#
# except TypeError:
#     print('Encountered Error')
#
# if currentX == 0:
#     if currentY == 0:  # top left corner
#         futureX = -1
#         futureY = -1  # moves to bottom right
#
#     else:  # bottom left corner
#         futureX = -1
#         futureY = 0  # moves to top right
#
# elif currentX == len(currentState[0]) - 1:
#
#     if currentY == 0:  # top right corner
#         futureX = 0
#         futureY = -1  # moves to bottom left
#
#     else:  # bottom right corner
#         futureX = 0
#         futureY = 0  # moves to top left
