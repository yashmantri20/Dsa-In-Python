# Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = []
        intervals = sorted(intervals)
        a = intervals[0]
        for i in range(1,len(intervals)):
            if a[1] >= intervals[i][0]:
                a = [a[0],max(intervals[i][1],a[1])]
            else:
                l.append(a)
                a = intervals[i]
        l.append(a)
        return l

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged