# topological sorted course

from collections import deque, defaultdict

def topsort(vertices, edges):

    # initialize
    graph = defaultdict(list)
    in_degrees = {}

    # build graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        in_degrees[edge[1]] = in_degrees.get(edge[1], 0) + 1

    # find sources
    sources = deque([v for v in graph if v not in in_degrees])

    # sort
    sortedOrder = []
    while sources:
        node = sources.popleft()
        sortedOrder.append(node)

        for child in graph[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child) 

    # check for cycle
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

t2 = [
    ['cs01', 'cs02'],
    ['cs02', 'cs03'],
    ['cs03', 'cs01']
]

assert topsort(11, t1) == ['M1', 'M2', 'CS', 'A1', 'DS', 'MS', 'D1', 'BF', 'Q1', 'ST', 'GC']
assert topsort(3, t2) == []