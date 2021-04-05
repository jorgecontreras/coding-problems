# plus one

'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

def plus_one(digits):

    if len(digits) == 0:
        return [1]

    rightmost = len(digits) - 1
    if digits[rightmost] < 9:
        digits[rightmost] += 1
    else:
        return plus_one(digits[:-1]) + [0]

    return digits


assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([1,2,9]) == [1,3,0]
assert plus_one([9,9,9]) == [1,0,0,0]
assert plus_one([9]) == [1,0]
assert plus_one([0]) == [1]

print("all tests passed.")