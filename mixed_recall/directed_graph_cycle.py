# FIND CYCLE IN A DIRECTED GRAPH

def cycle(graph):

    # white, gray, black algorithm
    visited = set()
    for node in graph:
        if dfs(node, graph, visited, set()):
            return True

    return False


def dfs(node, graph, visited, visiting):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)
    for neighbor in graph[node]:
        if dfs(neighbor, graph, visited, visiting):
            return True

    visiting.remove(node)
    visited.add(node)

    return False