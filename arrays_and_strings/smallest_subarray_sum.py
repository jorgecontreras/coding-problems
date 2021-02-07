# smallest subarray with given sum

import math 

def smallest_subarray_with_given_sum(s, arr):
  smallest = math.inf
  l = r = 0
  value = 0
  
  for r in range(len(arr)):
    value += arr[r]
    while value >= s:
      smallest = min(smallest, r-l + 1)
      value -= arr[l]
      l += 1
      
  if smallest == math.inf:
    return 0 

  return smallest