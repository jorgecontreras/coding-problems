# MOST PEOPLE ALIVE
#
# Given a list of people with their birth and death year, find year with the most people alive. 
#
# A person's life can be seen as an interval. 
# Similar to the meeting rooms problem, we need to find the overlapping intervals.
# A heap is an ideal data structure that we will use to add and remove persons.
# The max length reached by the heap is our answer.
#
# Time complexity: O(NlogN), sorting takes NlogN and then we traverse the whole data: N + NlogN
# Space complexity: O(N), to store all the people alive at the same time
#
from heapq import *

def most_populated_year(data):
    # sort by birth year
    data.sort(key=lambda x: x[0])

    # initialize
    heap = []
    max_population = 0

    # traverse data
    for p in data:
        # remove people that have already died
        while heap and heap[0] < p[0]:
            heappop(heap)

        # insert this person into the heap
        heappush(heap, p[1])

        # keep track of size of heap, remembering the largest 
        max_population = max(max_population, len(heap))

    # the answer if the max size reached by our heap during the traversal
    return max_population

data = [
    [1900,1953], 
    [1920,1963],
    [1918,1944],
    [1890,1932],
    [1923,1969],
    [1955,1988],
    [1886,1977],
    [1910,1966],
    [1925,1985],
    [1926,1975],
    [1825,1865],
]

assert most_populated_year(data) == 9

print("all tests passed.")