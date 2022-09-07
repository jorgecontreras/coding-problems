# SHORTEST PATH
"""
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
The function should return the length of the shortest path between A and B. 
Consider the length as the number of edges in the path, not the number of nodes. 
If there is no path between A and B, then return -1.
"""

# Use BFS approach
# hint: in the BFS queue, store the accumulated distance to get to the node

from collections import deque, defaultdict

def shortest_path(edges, nodeA, nodeB):
    graph = build_graph(edges)

    # initialize the queue with the source node and distance 0
    queue = deque([(nodeA, 0)])

    visited = set()
    while queue:
        node, distance = queue.popleft()
        if node == nodeB:
            return distance

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return -1


def build_graph(edges):
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph

edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

assert shortest_path(edges, 'm', 's') == 6

print("All tests passed!")
