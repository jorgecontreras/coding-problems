# 3 SUM

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

def threeSum(nums):
    triplets = set()
    dups = set()
    seen = {}

    for i, n1 in enumerate(nums):
        if n1 in dups:
            continue # skip dups
        
        dups.add(n1)
        for j,n2 in enumerate(nums[i+1:]): 
            complement = -n1 -n2
            if complement in seen and seen[complement] == i:
                triplets.add(tuple(sorted([n1, n2, complement])))
            seen[n2] = i #mark the iteration where the element was encountered

    return triplets

print(threeSum([-1,0,1,2,-1,-4]))