import math
from heapq import *

def findMedian(arr):
  # keep two heaps
  top = [] # max heap
  bottom = [] # min heap
  output = []
  
  for n in arr:
    if top and n <= -top[0]:
      heappush(top, -n)
    else:
      heappush(bottom, n)
    
    # re balance heaps (both should have same size, or top bigger by 1)
    if len(top) > len(bottom):
      heappush(bottom, -heappop(top))

    elif len(bottom) > len(top):
      heappush(top, -heappop(bottom))
      
    # append next  
    if len(bottom) > len(top):
        output.append(bottom[0])
    elif len(top) > len(bottom):
        output.append(-top[0])
    else:
        output.append((-top[0] + bottom[0]) // 2)
      
  return output

# Tests
def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\033[92m' + '\u2713' + '\033[0m'
  wrongTick = '\033[91m' + '\u2717' + '\033[0m'
  if result:
    print(rightTick, ' Test #' ,test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)