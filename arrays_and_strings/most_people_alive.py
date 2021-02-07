# most people alive

# list of people with birth and death year. find year with the most people alive 

from heapq import *

def most_populated_year(data):
    data.sort(key=lambda x: x[0])

    heap = []
    max_population = 0

    for p in data:
        while heap and heap[0] < p[0]:
            heappop(heap)

        heappush(heap, p[1])
        max_population = max(max_population, len(heap))

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

print(most_populated_year(data))