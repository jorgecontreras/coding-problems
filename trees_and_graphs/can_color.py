# CAN COLOR?
"""
Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph. 
The function should return a boolean indicating whether or not it is possible to color nodes 
of the graph using two colors in such a way that adjacent nodes are always different colors.
"""
# Time complexity: O(e) - traverse all edges
# Space complexity: O(n) - store all nodes in the painted dictionary

# The "colors" can be represented with a boolean, since there are only two color options.

def can_color(graph):
    painted = {}
    # this iterative loop is important so that we can hop to 
    # a disconnected component
    for node in graph:
        if node in painted:
            continue

        # as soon as we find a component that broke the rule
        # we stop iterating and return early
        if paint(node, graph, painted) == False:
            return False

    # everything was painted as required, return True
    return True
    
# helper function to traverse graph and mark nodes with certain color    
def paint(node, graph, painted, intended = True):
    # if the node we are visiting is already painted,
    # check whether it is the color we want it to be...
    if node in painted:
        return painted[node] == intended

    # paint the node
    painted[node] = intended 

    intended = not intended # <-- change paint color
    # paint all the neighbors with the new color
    for neighbor in graph[node]:
        if paint(neighbor, graph, painted, intended) == False:
            return False

    return True

test1 = can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
}) 

test2 = can_color({
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
})

test3 = can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a"],
  "d": ["a"],
}) 

assert test1 == True
assert test2 == False
assert test3 == True

print("All tests passed!")