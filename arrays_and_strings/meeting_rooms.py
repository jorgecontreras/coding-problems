# 253. Meeting Rooms II
#
# Time complexity: O(NlogN)
# Space complexity O(N)
#
# Intuition:
#
# The number of rooms required increases when meetings overlap.
# To check if two meetings overlap we can use the end and start time.
# We will iterate over the intervals and check on each meeting if there are meetings going on.
# If there are meetings, we'll check and remove the ones that have already finished.
# Once we remove all the finished meetings, then we proceed to schedule the new meeting.
#
# The number of rooms required is the max number reached by our schedule. i.e. the max number of meetings that overlapped during the day
# The ideal data structure to store the meetings is a HEAP, because we will want to remove the meetings with the LOWEST endtime time first.

from heapq import *

def rooms_required(intervals):

    # sort intervals by start time
    intervals.sort(key= lambda x: x[0])

    # keep meeting ending times in a heap
    schedule = []

    # keep track of the max size o the heap
    rooms = 0

    # check all meetings for the day
    for meeting in intervals:
        # remove meetings that have ended before start time of this meeting (if any)
        while schedule and schedule[0] <= meeting[0]:
            heappop(schedule)

        # schedule the meeting and keep ending time 
        heappush(schedule, meeting[1])

        rooms = max(rooms, len(schedule))

    return rooms

intervals_1 = [[0,30],[5,10],[15,20]]
intervals_2 = [[7,10],[2,4]]

assert rooms_required(intervals_1) == 2
assert rooms_required(intervals_2) == 1

print("all tests passed.")