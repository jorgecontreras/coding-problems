# Product except self
#
# LeetCode 238 https://leetcode.com/problems/product-of-array-except-self/
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Solution:
# Get the products in two passes. 
# first pass: products to the left
# second pass: products to the right
#
# Time complexity: O(N)
# Space complexity: O(N)

def product_except_self(nums):
    result = [1]

    # first pass: get the product of the left-side elements
    p = 1
    for i in range(1, len(nums)):
        p *= nums[i-1]
        result.append(p)
    
    # second pass: get the product of the right-side elements and update the result array
    p = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= p
        p *= nums[i]

    return result
    
t1 = [1,2,3,4]
t2 = [2,1,0,8]
t3 = [1,2]

assert product_except_self(t1) == [24,12,8,6]
assert product_except_self(t2) == [0,0,16,0]
assert product_except_self(t3) == [2,1]

print("tests passed.")