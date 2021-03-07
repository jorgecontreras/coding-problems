# Find connected nodes BFS 

from collections import deque, defaultdict

def find_connected(edges):
    graph = defaultdict(list)

    # build the undirected graph - add both edges
    for e0, e1 in edges:
        graph[e0].append(e1)
        graph[e1].append(e0)

    # find the connected nodes
    visited = set()
    components = []

    for node in graph:
        queue = deque([node])
        component = []
        while queue:
            size = len(queue)
            for _ in range(size):
                n = queue.popleft()
                if n in visited:
                    continue
                visited.add(n)
                component.append(n)
                queue += graph[n]

        if component:
            components.append(component)

    return components
            
edges = [
    [1,0],
    [1,8],
    [4,5],
    [6,2],
    [2,4],
    [5,2],
    [9,9],
    [9,13],
    [16,12],
    [12,0]
]

groups = find_connected(edges)

print(groups)

assert groups == [[1, 0, 8, 12, 16], [4, 5, 2, 6], [9, 13]]

print("all tests passed.")