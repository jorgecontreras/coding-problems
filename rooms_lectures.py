# MINIMUM NUMBER OF ROOMS

"""
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.
"""

from heapq import *

def rooms(meetings):
    
    # sort by start time
    meetings.sort(key=lambda x: x[0])
    rooms = 0

    # create min heap to store active meetings
    heap = []

    # iterate through all meetings and add the to the heap
    for m in meetings:
        #remove meetings that have ended (end time <= start time of given meeting)
        while heap and heap[0] <= m[0]:
            heappop(heap)

        #add meeting to the heap
        heappush(heap, m[1]) 
        
        #keep max size of heap
        rooms = max(rooms, len(heap))

    # return max size of heap
    return rooms


t1 = [[1,4], [2,5], [7,9]]
t2 = [[6,7], [2,4], [8,12]]
t3 = [[1,4], [2,3], [3,6]]
t4 = [[4,5], [2,3], [2,4], [3,5]]

assert rooms(t1) == 2
assert rooms(t2) == 1
assert rooms(t3) == 2
assert rooms(t4) == 2