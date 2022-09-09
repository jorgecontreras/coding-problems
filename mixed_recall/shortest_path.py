# SHORTEST PATH
# distance of shortest path

from collections import deque

def shortest_path(graph, src, dst):
    queue = deque([(src, 0)])

    visited = set()
    
    while queue:
        node, distance = queue.popleft()
        if node == dst:
            return distance

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return -1
