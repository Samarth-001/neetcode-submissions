class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:x[0])
        
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if prevEnd <= start:
                prevEnd = end
                continue
            
            prevEnd = min(prevEnd, end)
            res+=1
        
        return res
            