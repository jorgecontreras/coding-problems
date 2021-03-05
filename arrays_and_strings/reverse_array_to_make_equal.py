"""
REVERSE TO MAKE EQUAL


PROBLEM STATEMENT:

Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.

Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]

output = true

Explanation:
After reversing the subarray of B from indices 1 to 3, array B will equal array A.

"""

# ALGORITHM
#
# Two pointers
#  
# Check one by one and stop left pointer on the first difference
#
# Move right pointer from right to left until we find a match
#   v       
# 1,2,3,4,2,4,7,2
#
#               v
# 1,4,2,4,3,2,7,2   Check if the reverse of subarray from left to right in Array A is equal to subarray from left to right in Array B
#                   If equal then proceed and reverse the actual elements.
#
#           v
# 1,4,2,4,3,2,7,2  Otherwise, keep moving right pointer to the left until we find another match and try again the previous step.
#                  
#                  Keep going for the rest of the elements.

def are_they_equal(array_a, array_b):
  
  right = len(array_a) - 1
  
  i = 0
  while i < len(array_a): 
    # check one by one 
    if array_a[i] != array_b[i]:
      #stop pointer one on the first difference
      while right > i:
        #try to reverse from each match found, comparing left and right pointers
        if array_b[right] == array_a[i]:
          if array_b[i:right+1] == array_a[i:right+1][::-1]:
            array_b[i:right+1] = array_b[i:right+1][::-1]
            i = right
            break
        
        #prev try did not work, move right pointer to next match
        right -= 1
          
    # keep going 
    i += 1

  return array_a == array_b


def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)