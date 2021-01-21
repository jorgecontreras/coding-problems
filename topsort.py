# topological sort

# 1) Initialization
# 2) Build the graph and find in-degrees of all vertices
# 3) Find all sources
# 4) Sort
#
# in-degree is the number of incoming edges of a vertex
#
# Time complexity:
# O(V+E)
#
# Space complexity:
# O(V+E)
#

from collections import deque

def topsort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # 1. Initialization
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # 2. build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child] += 1

    # 3. find all sources
    sources = deque()
    for node in inDegree:
        if inDegree[node] == 0:
            sources.append(node)

    # 4. sort
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        # get the node's children to decrement their in-degrees
        for child in graph[vertex]:
            inDegree[child] -= 1
            # if no more indegrees, then it becomes a source, queue it
            if inDegree[child] == 0:
                sources.append(child)

    # Exceptions
    # topological sort is not possible if graph has cycle
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder

graph = [[3,2], [3,0], [2,0], [2,1]]
topsorted = topsort(4, graph)

print(topsorted)