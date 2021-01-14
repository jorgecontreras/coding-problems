
# PROBLEM STATEMENT.
#
# You are given a 2-D matrix where each cell consists of either /, \, or an empty space. 
# Write an algorithm that determines into how many regions the slashes divide the space.
# 
# For example, suppose the input for a three-by-six grid is the following:
#
# \    /
#  \  /
#   \/
#
# Considering the edges of the matrix as boundaries, this divides the grid into three triangles, so you should return 3.

# idea:
# the problem of counting regions can be transformed into a problem of counting islands
#
# 1. The input grid will be expanded (multiplied in size by 3)
# 2. the characters will be converted to 1s and 0s.
# 
# so, the example above will be represented something like this:
#
#  011111110
#  101111101
#  110111011
#  111010111
#  111101111
#
# 3. count the "islands" or "regions" of 1s using DFS
#

# helper DFS function to count regions
def dfs(matrix, i, j):
    if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j] != 1: # out of bounds or not a region
        return

    matrix[i][j] = 0 # visited node should be set as '0' to mark as visited node.

    dfs(matrix, i+1, j) # explore right adjacent cell
    dfs(matrix, i-1, j) # explore left adjacent cell
    dfs(matrix, i, j+1) # explore bottom adjacent cell
    dfs(matrix, i, j-1) # explor top adjacent

def count_regions(matrix):

    if not matrix:
        return 

    # expand matrix (increase resolution)
    res = 3
    n = len(matrix) * res
    grid = []

    for _ in range(n):
        row = [1] * n
        grid.append(row)

    for i in range(len(matrix)):
        j = 0
        for c in matrix[i]:
            if c == "/":
                grid[i*res][j*res+2] = 0
                grid[i*res+1][j*res+1] = 0
                grid[i*res+2][j*res] = 0

            elif c == "\\":
                grid[i*res][j*res] = 0
                grid[i*res+1][j*res+1] = 0
                grid[i*res+2][j*res+2] = 0
            
            j += 1

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1: # it's a root node
                dfs(grid, row, col)
                count += 1
    return count


# 3 regions
t2 = [
  "//",
  "/ "
]

# 4 regions
t3 = [
  "\\/",
  "/\\"
]

# 5 regions
t4 = [
  "/\\",
  "\\/"
]

assert count_regions(t2) == 3
assert count_regions(t3) == 4
assert count_regions(t4) == 5
