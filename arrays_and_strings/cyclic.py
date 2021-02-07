# cyclic

# determine whether a graph contains a cycle or not

# For connections = [[1], [2], [3, 4], [4], [0]], the output should be
# hasDeadlock(connections) = true.

# For connections = [[1, 2, 3], [2, 3], [3], []], the output should be
# hasDeadlock(connections) = false

def hasDeadlock(connections):
    white = set([x for x in range(len(connections))])

    def search(loc, path = set()):
        print(loc)
        if loc not in white: return False
        if loc in path: return True
        for conn in connections[loc]:
            next_path = set(path)
            next_path.add(loc)
            if search(conn, next_path):
                return True
        white.remove(loc)
        return(False)

    while white:
        for next_pos in white: 
            break
        if search(next_pos): 
            return True

    return(False)

connections = [[1], [2], [3, 4], [4], [0]]
result = hasDeadlock(connections)
print(result)

connections = [[1, 2, 3], [2, 3], [3], []]
result = hasDeadlock(connections)
print(result)