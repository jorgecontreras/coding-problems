# merge intervals

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def show(self):
        print("[{start}, {end}]". format(start=self.start, end=self.end))

def merge(intervals):

    # at least 2 intervals
    if len(intervals) < 2:
        return intervals

    # sort by start
    intervals.sort(key=lambda x:x.start)

    # initialize
    merged = []
    start = intervals[0].start
    end = intervals[0].end

    # iterate
    for i in range(1, len(intervals)):
        # if there is an overlap, adjust end
        if intervals[i].start <= end: 
            end = max(intervals[i].end, end)
        else: # no overlap, 
            # append interval
            merged.append(Interval(start, end))
            
            #initialize next range
            start = intervals[i].start 
            end = intervals[i].end

    #append last one
    merged.append(Interval(start, end)) 

    return merged