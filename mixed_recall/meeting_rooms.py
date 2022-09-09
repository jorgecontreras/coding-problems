# MEETING ROOMS
from heapq import *

def meeting_rooms(meetings):
    heap = []

    # sort meetings by start time
    meetings = sorted(meetings, key= lambda x:x[0])

    rooms = 0
    for meeting in meetings:
        while heap and heap[0] <= meeting[0]:
            heappop(heap)

        heappush(heap, meeting[1])
        rooms = max(rooms, len(heap))

    return rooms

meetings = [
    (11,15),
    (16,18),
    (17,20),
    (9,10),
    (12,14),
    (18,22),
    (19,20)
]

rooms = meeting_rooms(meetings)

print(rooms) #3