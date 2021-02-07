# queue removals

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
from collections import deque
from heapq import *

def findPositions(arr, x):
  # Write your code here
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