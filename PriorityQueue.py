import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):

        # for x in self._queue:   #if the state already exists but the new item has a lower cost, replace old item with new item with lower cost
        #     if item.state == x[2].state and item.totalCost < x[2].totalCost:
        #         self._queue.remove(x)
        #
        # heapq.heappush(self._queue, (priority, self._index, item))

        if item.state not in self.getStates():
            heapq.heappush(self._queue, (priority, self._index, item))
            self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def getStates(self):
        tempList = []

        for x in self._queue:
            tempList.append(x[2].state)

        return tempList

    def toString(self):

        returnString = ''
        for x in self._queue:
            returnString += x[2].getString()

        return returnString


