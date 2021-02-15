# FRUITS INTO BASKETS
#
# Problem Statement:
#
# Given an array of characters where each character represents a fruit tree, you are given two baskets, 
# and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but you can’t skip a tree once you have started. 
# You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both the baskets.
#
# Intuition:
# In other words, we are looking for the longest subarray with at most two distinct elements
#
# This problem can be solved using the sliding window pattern.
#
# Algorithm:
# Open the window
# Start storing the "fruits" into a dictionary.
# Keep moving forward until dictionary length goes over 2, which means we have reached more that 2 type of fruits.
# start closing the window, decreasing and eventually removing one element of the dictionary.
# Store the size of the subarray we reached at that point
# Continue with remaining elements
#
# Time complexity: O(N), we need to traverse all elements once.
# Space complexity: O(1), there will be at most 3 types of fruits stored at a time.

def solve(fruits):

    largest = 0
    distinct = {}
    start = 0 

    for i in range(len(fruits)):
        f = fruits[i]
        distinct[f] = distinct.get(f, 0) + 1

        while len(distinct) > 2:
            #largest = max(largest, i-start)
            remove = fruits[start]
            distinct[remove] -= 1
            if distinct[remove] == 0:
                del distinct[remove]
            start += 1
        
        largest = max(largest, i-start+1)

    return largest 

t1 = ['A', 'B', 'C', 'A', 'C']
o1 = 3

t2 = ['B', 'C', 'B', 'B', 'C', 'A']
o2 = 5

print(solve(t1))
print(solve(t2))
