# count number of islands
# 
# PROBLEM STATEMENT.
#
# Given an m x n 2D grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# 
# Example 1:
# 
# Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
# ]
# Output: 1
#
# 
# Example 2:
#
# Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]
# Output: 3

# helper depth first search function
def dfs(matrix, i, j):
    if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j] != 1: # out of bounds or not an island
        return

    matrix[i][j] = 0 # visited node should be set as '0' to mark as visited node.

    dfs(matrix, i+1, j) # explore right adjacent cell
    dfs(matrix, i-1, j) # explore left adjacent cell
    dfs(matrix, i, j+1) # explore bottom adjacent cell
    dfs(matrix, i, j-1) # explor top adjacent

# Algorithm
#
# Linear scan the 2D grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search. 
# During DFS, every visited node should be set as '0' to mark as visited node. 
# Count the number of root nodes that trigger DFS, this number would be the number of islands 
# since each DFS starting at some root identifies an island.
# 
def number_of_islands_dfs(matrix):

    if not matrix:
        return 

    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1: # it's a root node
                dfs(matrix, row, col)
                count += 1
    return count

# tests
test_1 = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]

test_2 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

t1_result = number_of_islands_dfs(test_1)
t2_result = number_of_islands_dfs(test_2)

print(t1_result)
print(t2_result)