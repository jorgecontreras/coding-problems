# overlapping lectures

# [0, 50]
# [30, 75]
# [60, 150]

from heapq import *

def rooms(intervals):
    # sort lectures by start time
    intervals.sort(key=lambda x: x[0])

    heap = [] #75
    rooms = 0 #2

    for i in intervals:
        while heap and heap[0] <= i[0]:
            heappop(heap)

        heappush(heap, i[1])
        rooms = max(rooms, len(heap))

    return rooms

intervals = [
    [0, 50],
    [30, 75],
    [60, 150]
]

print(rooms(intervals))



