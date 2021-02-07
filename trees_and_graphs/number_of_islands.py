# number of islands

def dfs(grid, y, x):
    
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == "0":
        return

    grid[y][x] = "0"

    #search adjacent cells
    # left
    dfs(grid, y-1, x)
    dfs(grid, y+1, x)
    dfs(grid, y, x-1)
    dfs(grid, y, x+1)

    

def number_of_islands(grid):

    #iterate grid and trigger dfs if land (1) found
    height = len(grid)
    width = len(grid[0])

    count = 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] == "1": #land found
                dfs(grid, row, col)
                count += 1

    return count

t1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(number_of_islands(t1))