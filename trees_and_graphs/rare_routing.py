# RARE ROUTING

"""
Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples where each tuple represents a direct road that connects a pair of cities. 
The function should return a boolean indicating whether or not there exists a unique route for every pair of cities. 
A route is a sequence of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means if there is a road between A and B, then you can use that road to go from A to B or go from B to A.
"""

# 1. This is a graph problem.
# 2. The key to the solution is to detect an UNIDRECTED CYCLE. It's not the same as the directed cycle,
# in which case we would use the white-gray-black algorithm. Instead we just need to track the last
# visited node so we dont go back to it 

# Time complexity: O(E) - use all of the vertices
# Space complexity: O(N) - create the adjacency list

def rare_routing(n, roads):
    graph = build_graph(n, roads)

    # start my trip at city 0
    visited = set()
    if not travel(0, graph, visited, 0):
        return False

    # confirm all cities were visited
    return len(visited) == n

def travel(node, graph, visited, origin):
    if node in visited:
        return False

    visited.add(node)
    for neighbor in graph[node]:
        # dont go back to where we came from:
        if neighbor == origin:
            continue

        if not travel(neighbor, graph, visited, node):
            return False

    return True

def build_graph(n, edges):
    """
    edge list needs to be converted to adjacency list
    """
    graph = {}
    for i in range(n):
        graph[i] = []

    # two way street: undirected
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph

assert rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
]) == True

assert rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3),
  (3, 2)
]) == False 

assert rare_routing(6, [
  (1, 2),
  (4, 1),
  (5, 4),
  (3, 0),
  (0, 1),
  (0, 4),
]) == False

rare_routing(4, [
  (0, 1),
  (3, 2),
]) == False

print("All tests passed!")