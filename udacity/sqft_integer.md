# Square root of an integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))

# Solution

Implemented a binary search to find the most accurante result

# Time Complexity

The total number of possibilities is cut by half on every iteration, which means we have a complexity of **O(log(n))**

# Space complexity

This algorithm will require space to store the number of possibilities, with a space of **O(n)**