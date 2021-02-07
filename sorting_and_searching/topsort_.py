# initialize
# build graph 
# find sources
# sort

from collections import deque

def topsort(vertices, edges):
    sortedOrder = []

    # initialize
    inDegrees = {}
    graph = {}

    # build graph
    for edge in edges:
        parent, child = edge[0], edge[1]

        if parent in graph:
            graph[parent].append(child)
        else:
            graph[parent] = [child]
            
        inDegrees[child] = inDegrees.get(child, 0) + 1

    # find sources
    sources = deque()
    sources_unique = set()
    for edge in edges:
        if edge[0] not in inDegrees and edge[0] not in sources_unique:
            sources.append(edge[0])
            sources_unique.add(edge[0])

    # sort
    while len(sources) > 0:
        s = sources.popleft()
        sortedOrder.append(s)
        if s in graph:
            for child in graph[s]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0: # becomes a source
                    sources.append(child)

    # check cycle
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder

t1 = [
    ['M1', 'M2'],
    ['M1', 'CS'],
    ['CS', 'A1'],
    ['CS', 'DS'],
    ['A1', 'MS'],
    ['A1', 'D1'],
    ['A1', 'BF'],
    ['DS', 'Q1'],
    ['DS', 'ST'],
    ['A1', 'GC'],
    ['DS', 'GC']
]

topsorted = topsort(11, t1)

print(topsorted)