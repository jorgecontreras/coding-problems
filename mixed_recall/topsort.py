# Topological Sort
from collections import defaultdict

def topsort(n, edges):
    # convert list of edges to adjacency list
    graph = build_graph(n, edges)

    # DFS
    order = []
    visited = set() # O(1) lookup of elements
    for node in graph:
        order += dfs(node, graph, visited, [])

    # cycle?
    if len(visited) != n:
        return []

    return order[::-1]

def dfs(source, graph, visited, order):
    """
    return a list of nodes from edge of graph to the starting node
    """
    if source in visited:
        return []

    visited.add(source)
    for neighbor in graph[source]:
        dfs(neighbor, graph, visited, order)

    order.append(source)
    return order

def build_graph(n, edges):
    
    graph = {}
    for i in range(n):
        graph[i] = []

    for a, b in edges:
        graph[a].append(b)

    return graph

edges = [
    (8, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (4, 6),
    (4, 5),
    (6, 7),
    (7, 0)
]

n = 9
order = topsort(n, edges)

print(order)