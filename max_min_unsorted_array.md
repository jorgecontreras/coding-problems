# Max and Min in a Unsorted array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

# solution

Initialize smallest and largest with the first element. then keep comparing each number, updating the values of these two variables.

# time complexity

**O(N)** because we traverse all the elements in the list once.

# space complexity

**O(1)** because no additional storage is required (other than the two vars smallest and largest) 