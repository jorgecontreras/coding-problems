# INSERT INTERVAL
#
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Time complexity: O(N)
# Space complexity: O(N)
#
def insert_interval(intervals, new_interval):
    
    i = 0
    n = len(intervals)

    ans = []

    # insert intervals that start before the new interval
    while i < n and new_interval[0] > intervals[i][0]:
        ans.append(intervals[i])
        i += 1

    # if no overlap, insert interval
    if not ans or ans[-1][1] < new_interval[0]:
        ans.append(new_interval)

    # if there's overlap, merge with last interval
    if new_interval[0] <= ans[-1][1]:
        ans[-1][1] = max(ans[-1][1], new_interval[1])

    # add next intervals, merging if needed
    while i < n:
        if intervals[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        else:
            ans.append(intervals[i])
        i += 1
    return ans
    

t1 = [[1,3], [6,9]]
i1 = [2,5]

t2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
i2 = [4,8]

t3 = []
i3 = [5,7]

t4 = [[1,5]]
i4 = [2,3]

t5 = [[1,5]]
i5 = [2,7]

t6 = [[1,5]]
i6 = [6,8]

t7 = [[1,5]]
i7 = [0,3]

assert insert_interval(t1, i1) == [[1,5], [6,9]]
assert insert_interval(t2, i2) == [[1,2], [3,10], [12,16]]
assert insert_interval(t3, i3) == [[5,7]]
assert insert_interval(t4, i4) == [[1,5]]
assert insert_interval(t5, i5) == [[1,7]]
assert insert_interval(t6, i6) == [[1,5], [6,8]]
assert insert_interval(t7, i7) == [[0,5]]

print("all tests passed.")