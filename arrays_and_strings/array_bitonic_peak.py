# array bitonic max

"""
Problem Statement #
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Example 1:

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.
Example 2:

Input: [3, 8, 3, 1]
Output: 8
Example 3:

Input: [1, 3, 8, 12]
Output: 12
Example 4:

Input: [10, 9, 8]
Output: 10
"""

def find_max_in_bitonic_array(nums):
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end-start) // 2

        #if we are in descendind part, go left
        if nums[mid] > nums[mid+1]: 
            end = mid 
        #otherwise, go right
        else:
            start = mid + 1

    return nums[start]

def main():
  assert find_max_in_bitonic_array([3, 4, 5, 1]) == 5
  assert find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]) == 12
  assert find_max_in_bitonic_array([3, 8, 3, 1]) == 8
  assert find_max_in_bitonic_array([1, 3, 8, 12]) == 12
  assert find_max_in_bitonic_array([10, 9, 8]) == 10
  assert find_max_in_bitonic_array([2, 23]) == 23
  assert find_max_in_bitonic_array([0]) == 0
  assert find_max_in_bitonic_array([-2, 0, 3, 5, 3, -1]) == 5

  print("all tests passed.")


main()
