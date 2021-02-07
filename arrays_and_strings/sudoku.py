def sudoku2(grid):
    
    grid_x = [['.' for _ in range(9)] for _ in range(9)]
    grid_3 = [[set() for _ in range(3)] for _ in range(3)]
    
    # check rows
    for i, r in enumerate(grid):
        tc = set()
        n = i // 3
        for j, c in enumerate(r):
            grid_x[j][i] = c 
            if c != '.' and c in tc:
                return False
            else:
                tc.add(c)
        
            m = j // 3
            
            # check 3x3
            if c != '.' and c in grid_3[n][m]:
                return False
            else:
                grid_3[n][m].add(c)
    
    # check cols
    for i, r in enumerate(grid_x):
        tc = set()
        for j, c in enumerate(r):
            if c != '.' and c in tc:
                return False
            else:
                tc.add(c)
                
    return True
