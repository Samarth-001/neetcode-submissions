
import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        # Minimum effort required to reach each cell
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        heap = [(0,0,0)]

        while heap:
            effort, row, col = heapq.heappop(heap)

            if effort > dist[row][col]:
                continue
            
            if row == rows-1 and col == cols-1:
                return effort
            
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            for i,j in directions:
                ni = row + i
                nj = col + j

                if 0<=ni<rows and 0<=nj<cols:
                    difference = abs(heights[ni][nj] - heights[row][col])

                    new_effort = max(effort, difference)

                    if new_effort < dist[ni][nj]:
                        dist[ni][nj] = new_effort
                        heapq.heappush(heap, (new_effort, ni, nj))
        
        return 0
                