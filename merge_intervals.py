# Merge intervals

def merge_intervals(intervals):

    if len(intervals) < 2:
        return intervals

    # sort intervals by start
    intervals.sort(key= lambda x: x[0])

    merged = []

    # get start and end of First interval
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= end: #overlap
            #adjust the end of the interval
            end = max(intervals[i][1], end)
        else: # no overlap
            # append new interval
            merged.append([start, end])

            # get start and end of Current Interval
            start = intervals[i][0]
            end = intervals[i][1]

    merged.append([start, end])
    return merged

t1 = [
    [1,4],
    [2,5],
    [7,9]
]

t2 = [
    [6,7],
    [2,4],
    [5,9]
]

t3 = [
    [1,4],
    [2,6],
    [3,5]
]

print(merge_intervals(t1))
print(merge_intervals(t2))
print(merge_intervals(t3))