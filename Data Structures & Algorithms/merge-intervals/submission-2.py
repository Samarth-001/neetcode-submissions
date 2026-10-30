class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        istart = intervals[0][0]
        iend = intervals[0][1]

        output = []

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start <= iend:
                iend = max(end,iend)
            else:
                output.append([istart,iend])
                istart = start
                iend = max(end,iend)
        output.append([istart,iend])
        
        return output