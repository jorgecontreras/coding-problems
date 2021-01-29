# bitonic array search
# Time complexity: O(logN)
# Space complexity: O(1)

"""
Search Bitonic Array (medium) #
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3
Example 2:

Input: [3, 8, 3, 1], key=8
Output: 1
Example 3:

Input: [1, 3, 8, 12], key=12
Output: 3
Example 4:

Input: [10, 9, 8], key=10
Output: 0
"""

def search_bitonic_array(nums, key):
    #find peak element
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end-start) // 2

        if nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid + 1

    peak = start

    #left side as an asc order array
    start, end = 0, peak
    while start <= end:
        mid = start + (end-start) // 2

        if nums[mid] == key:
            return mid

        elif nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    #key wasnt found on left side, now try right side
    #right side is a desc order array
    start, end = peak, len(nums) - 1
    while start <= end:
        mid = start + (end-start) // 2

        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            end = mid - 1
        else:
            start = mid + 1

    # not found anywhere
    return -1


def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 8))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()