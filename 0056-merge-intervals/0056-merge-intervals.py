class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1,n):
            s = intervals[i][0]
            e = intervals[i][1]

            last_end = res[-1][1] #res[-1][1] is last end interval in res

            if s <= last_end:   
                res[-1][1] = max(last_end,e)
            else:
                res.append([s,e])

        return res
