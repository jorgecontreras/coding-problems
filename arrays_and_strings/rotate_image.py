# ROTATE IMAGE
#
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#

# Rotate using extra space
def rotate(matrix):
    
    rotated = []
    for j in range(len(matrix)):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        
        rotated.append(new_row[::-1])

    return rotated

# Rotate in place can be done in two steps:
# 1. transpose: mirror elements along the diagonal
# 2. reflect: mirror elements vertically

def rotate_in_place(matrix):
    transpose(matrix)
    reflect(matrix)
    return matrix

def transpose(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

def reflect(matrix):
    
    for i in range(len(matrix)):
        left, right = 0, len(matrix) - 1

        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

t1 = [[1,2,3],[4,5,6],[7,8,9]]
t2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
t3 = [[1]]
t4 = [[1,2],[3,4]]

assert rotate(t1) == rotate_in_place(t1)
assert rotate(t2) == rotate_in_place(t2)
assert rotate(t3) == rotate_in_place(t3)
assert rotate(t4) == rotate_in_place(t4)

print("all tests passed.")