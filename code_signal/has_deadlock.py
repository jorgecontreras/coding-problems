def hasDeadlock(connections):

    unchecked = set([x for x in range(len(connections))])

    def search(loc, path = set()):
        if loc not in unchecked: 
            return False
            
        if loc in path: 
            return True
            
        for conn in connections[loc]:
            next_path = set(path)
            next_path.add(loc)
            if search(conn, next_path):
                return True
                
        unchecked.remove(loc)
        
        return False

    while unchecked:
        for next_pos in unchecked: 
            break
            
        if search(next_pos): 
            return True

    return False
