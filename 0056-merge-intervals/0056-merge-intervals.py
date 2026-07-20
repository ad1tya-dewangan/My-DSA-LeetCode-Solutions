# Sort intervals by their start time so overlapping intervals become adjacent.
# Add the first interval to the result.
# Compare each remaining interval with the last merged interval.
# If the current interval starts before the last merged interval ends,
# merge them by extending the end.
# Otherwise, add the current interval as a new merged interval.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1,n):
            s = intervals[i][0]  #start interval
            e = intervals[i][1]  #end interval

            last_end = res[-1][1] #res[-1][1] is last end interval in res

            if s <= last_end:   
                res[-1][1] = max(last_end,e)
            else:
                res.append([s,e])

        return res
