# MERGE INTERVALS
#
# Time complexity: O(NlogN) - traverse all elements (N) and the initial sorting (logN)
# Space complexity: O(N) - the merged output will require N space
# 
# Given a list of intervals, merge all the overlapping intervals to produce a list that has onlu mutually exclusive intervals.

from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  
  if len(intervals) < 2:
    return intervals
  
  # sort by start
  intervals.sort(key=lambda x: x.start)

  merged = []
  start = intervals[0].start
  end = intervals[0].end

  for i in range(1, len(intervals)):
      if intervals[i].start <= end:
          end = max(intervals[i].end, end)
      else:
          merged.append(Interval(start, end))
          start = intervals[i].start
          end = intervals[i].end

  merged.append(Interval(start, end))
  return merged

def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()