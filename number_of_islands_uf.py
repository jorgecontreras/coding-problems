# number of islands - union find
class UnionFind:
    def __init__(self, grid):
        y = len(grid)
        x = len(grid[0])
        self.parents = [0] * (x*y)
        self.count = 0

        for i in range(y):
            for j in range(x):
                if grid[i][j] == 1:
                    self.parents[i*x+j] = -1
                    self.count += 1
    
    def find(self, n):
        if self.parents[n] < 0:
            return n
        else:
            self.parents[n] = self.find(self.parents[n]) 
            return self.parents[n]

    def union(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)
        
        if p1 == p2: # both already in same group
            return
        if self.parents[p1] > self.parents[p2]:
            p1,p2 = p2,p1
       
        self.parents[p1] += self.parents[p2] #union happens here
        self.parents[p2] = p1 # point to new parent
        self.count -= 1 
       
def number_of_islands_uf(grid):
    if not grid:
        return 0

    x = len(grid[0])
    y = len(grid)

    uf = UnionFind(grid)

    for i in range(y):
        for j in range(x):
            if grid[i][j] == 1: #land found
                # search adjacent cells
                for k,l in ([1,0], [-1,0], [0,1], [0,-1]):
                    ny, nx = i+k, j+l
                    #if adjacent cell is within bounds and is land, perform union
                    if 0 <= ny < y and 0 <= nx < x and grid[ny][nx] == 1: 
                        uf.union(i*x + j, ny*x + nx)
    
    return uf.count


t1 = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]

t2 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

assert number_of_islands_uf(t1) == 1
assert number_of_islands_uf(t2) == 3