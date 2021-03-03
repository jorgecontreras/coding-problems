# QUEUE REMOVALS

"""
You're given a list of n integers arr, which represent elements in a queue (in order from front to back). You're also given an integer x, and must perform x iterations of the following 3-step process:

Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it
For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue

Compute a list of x integers output, the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration.
"""

import math
from collections import deque
from heapq import *

def findPositions(arr, x):
  queue = deque()
  answer = []
  
  for i, n in enumerate(arr):
    queue.append((i+1, n))
      
  iterations = x
  while iterations > 0:
    remove = x
    decrement = []
    decremented = []
    largest = None
    while queue and remove > 0:
      o, p = queue.popleft()
      decrement.append((o, p))
      if not largest or p > largest[1]:
          largest = (o, p)
      remove -= 1
    
    # remove the tuple identified as largest
    answer.append(largest[0])
    decrement.remove(largest)
    
    for d in decrement:
        decremented.append((d[0], max(d[1]-1, 0)))

    queue += decremented
    iterations -= 1
  
  return answer

arr = [1, 2, 2, 3, 4, 5]
x = 5

print(findPositions(arr, x))
