# Rearrange array elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

# Solution

I have decided to use a MaxHeap to store the values. Then I keep polling the heap and add the elements intercalated into two variables.

# Time complexity

Heapify operation has a time complexity of O(logN) and since this has to be done for ever element inserted, the result is **O(NlogN)**

# Space complexity

The Heap will require additional space of the order **O(N)**