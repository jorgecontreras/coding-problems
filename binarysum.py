
graph = {
    4 : [2, 5],
    2 : [3, 6],
    5 : [9, 7],
    3 : [1, 8],
    6 : [4, 10]
}

visited = []

def dfs(visited, graph, node):

    
    if node not in visited:
        visited.append(node)
        print(node)
        for adjacent in graph[node]:
            dfs(visited, graph, adjacent)

dfs(visited, graph, 4)