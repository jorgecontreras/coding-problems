# array search rotated

"""
Search in Rotated Array (medium) #
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.


Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
"""

def search_rotated_array(nums, key):

    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (end-start) // 2
        if nums[mid] == key:
            return mid

        if nums[start] <= nums[mid]:
            #left half is ascending
            if key >= nums[start] and key < nums[mid]:
                #search in left
                end = mid - 1
            else:
                #search in right
                start = mid + 1
        else:
            #right half is ascending
            if key > nums[mid] and key <= nums[end]:
                #search in right
                start = mid + 1
            else:
                end = mid - 1
    
    return -1

def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()